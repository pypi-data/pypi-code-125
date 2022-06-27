"""Transform class definitions from the mypy AST form to IR."""

from abc import abstractmethod
from typing import Callable, List, Optional, Tuple
from typing_extensions import Final

from mypy.nodes import (
    ClassDef, FuncDef, OverloadedFuncDef, PassStmt, AssignmentStmt, CallExpr, NameExpr, StrExpr,
    ExpressionStmt, TempNode, Decorator, Lvalue, MemberExpr, RefExpr, TypeInfo, is_class_var
)
from mypy.types import Instance, get_proper_type, ENUM_REMOVED_PROPS
from mypyc.ir.ops import (
    Value, Register, Call, LoadErrorValue, LoadStatic, InitStatic, TupleSet, SetAttr, Return,
    BasicBlock, Branch, MethodCall, NAMESPACE_TYPE, LoadAddress
)
from mypyc.ir.rtypes import (
    RType, object_rprimitive, bool_rprimitive, dict_rprimitive, is_optional_type,
    is_object_rprimitive, is_none_rprimitive
)
from mypyc.ir.func_ir import FuncDecl, FuncSignature
from mypyc.ir.class_ir import ClassIR, NonExtClassInfo
from mypyc.primitives.generic_ops import py_setattr_op, py_hasattr_op
from mypyc.primitives.misc_ops import (
    dataclass_sleight_of_hand, pytype_from_template_op, py_calc_meta_op, type_object_op,
    not_implemented_op
)
from mypyc.primitives.dict_ops import dict_set_item_op, dict_new_op
from mypyc.irbuild.util import (
    is_dataclass_decorator, get_func_def, is_constant, dataclass_type
)
from mypyc.irbuild.builder import IRBuilder
from mypyc.irbuild.function import handle_ext_method, handle_non_ext_method, load_type


def transform_class_def(builder: IRBuilder, cdef: ClassDef) -> None:
    """Create IR for a class definition.

    This can generate both extension (native) and non-extension
    classes.  These are generated in very different ways. In the
    latter case we construct a Python type object at runtime by doing
    the equivalent of "type(name, bases, dict)" in IR. Extension
    classes are defined via C structs that are generated later in
    mypyc.codegen.emitclass.

    This is the main entry point to this module.
    """
    ir = builder.mapper.type_to_ir[cdef.info]

    # We do this check here because the base field of parent
    # classes aren't necessarily populated yet at
    # prepare_class_def time.
    if any(ir.base_mro[i].base != ir. base_mro[i + 1] for i in range(len(ir.base_mro) - 1)):
        builder.error("Non-trait MRO must be linear", cdef.line)

    if ir.allow_interpreted_subclasses:
        for parent in ir.mro:
            if not parent.allow_interpreted_subclasses:
                builder.error(
                    'Base class "{}" does not allow interpreted subclasses'.format(
                        parent.fullname), cdef.line)

    # Currently, we only create non-extension classes for classes that are
    # decorated or inherit from Enum. Classes decorated with @trait do not
    # apply here, and are handled in a different way.
    if ir.is_ext_class:
        cls_type = dataclass_type(cdef)
        if cls_type is None:
            cls_builder: ClassBuilder = ExtClassBuilder(builder, cdef)
        elif cls_type in ['dataclasses', 'attr-auto']:
            cls_builder = DataClassBuilder(builder, cdef)
        elif cls_type == 'attr':
            cls_builder = AttrsClassBuilder(builder, cdef)
        else:
            raise ValueError(cls_type)
    else:
        cls_builder = NonExtClassBuilder(builder, cdef)

    for stmt in cdef.defs.body:
        if isinstance(stmt, OverloadedFuncDef) and stmt.is_property:
            if isinstance(cls_builder, NonExtClassBuilder):
                # properties with both getters and setters in non_extension
                # classes not supported
                builder.error("Property setters not supported in non-extension classes",
                              stmt.line)
            for item in stmt.items:
                with builder.catch_errors(stmt.line):
                    cls_builder.add_method(get_func_def(item))
        elif isinstance(stmt, (FuncDef, Decorator, OverloadedFuncDef)):
            # Ignore plugin generated methods (since they have no
            # bodies to compile and will need to have the bodies
            # provided by some other mechanism.)
            if cdef.info.names[stmt.name].plugin_generated:
                continue
            with builder.catch_errors(stmt.line):
                cls_builder.add_method(get_func_def(stmt))
        elif isinstance(stmt, PassStmt):
            continue
        elif isinstance(stmt, AssignmentStmt):
            if len(stmt.lvalues) != 1:
                builder.error("Multiple assignment in class bodies not supported", stmt.line)
                continue
            lvalue = stmt.lvalues[0]
            if not isinstance(lvalue, NameExpr):
                builder.error("Only assignment to variables is supported in class bodies",
                              stmt.line)
                continue
            # We want to collect class variables in a dictionary for both real
            # non-extension classes and fake dataclass ones.
            cls_builder.add_attr(lvalue, stmt)

        elif isinstance(stmt, ExpressionStmt) and isinstance(stmt.expr, StrExpr):
            # Docstring. Ignore
            pass
        else:
            builder.error("Unsupported statement in class body", stmt.line)

    cls_builder.finalize(ir)


class ClassBuilder:
    """Create IR for a class definition.

    This is an abstract base class.
    """

    def __init__(self, builder: IRBuilder, cdef: ClassDef) -> None:
        self.builder = builder
        self.cdef = cdef
        self.attrs_to_cache: List[Tuple[Lvalue, RType]] = []

    @abstractmethod
    def add_method(self, fdef: FuncDef) -> None:
        """Add a method to the class IR"""

    @abstractmethod
    def add_attr(self, lvalue: NameExpr, stmt: AssignmentStmt) -> None:
        """Add an attribute to the class IR"""

    @abstractmethod
    def finalize(self, ir: ClassIR) -> None:
        """Perform any final operations to complete the class IR"""


class NonExtClassBuilder(ClassBuilder):
    def __init__(self, builder: IRBuilder, cdef: ClassDef) -> None:
        super().__init__(builder, cdef)
        self.non_ext = self.create_non_ext_info()

    def create_non_ext_info(self) -> NonExtClassInfo:
        non_ext_bases = populate_non_ext_bases(self.builder, self.cdef)
        non_ext_metaclass = find_non_ext_metaclass(self.builder, self.cdef, non_ext_bases)
        non_ext_dict = setup_non_ext_dict(self.builder, self.cdef, non_ext_metaclass,
                                          non_ext_bases)
        # We populate __annotations__ for non-extension classes
        # because dataclasses uses it to determine which attributes to compute on.
        # TODO: Maybe generate more precise types for annotations
        non_ext_anns = self.builder.call_c(dict_new_op, [], self.cdef.line)
        return NonExtClassInfo(non_ext_dict, non_ext_bases, non_ext_anns, non_ext_metaclass)

    def add_method(self, fdef: FuncDef) -> None:
        handle_non_ext_method(self.builder, self.non_ext, self.cdef, fdef)

    def add_attr(self, lvalue: NameExpr, stmt: AssignmentStmt) -> None:
        add_non_ext_class_attr_ann(self.builder, self.non_ext, lvalue, stmt)
        add_non_ext_class_attr(self.builder, self.non_ext, lvalue, stmt, self.cdef,
                               self.attrs_to_cache)

    def finalize(self, ir: ClassIR) -> None:
        # Dynamically create the class via the type constructor
        non_ext_class = load_non_ext_class(self.builder, ir, self.non_ext, self.cdef.line)
        non_ext_class = load_decorated_class(self.builder, self.cdef, non_ext_class)

        # Save the decorated class
        self.builder.add(InitStatic(non_ext_class, self.cdef.name, self.builder.module_name,
                                    NAMESPACE_TYPE))

        # Add the non-extension class to the dict
        self.builder.call_c(dict_set_item_op,
                            [
                                self.builder.load_globals_dict(),
                                self.builder.load_str(self.cdef.name),
                                non_ext_class
                            ], self.cdef.line)

        # Cache any cacheable class attributes
        cache_class_attrs(self.builder, self.attrs_to_cache, self.cdef)


class ExtClassBuilder(ClassBuilder):
    def __init__(self, builder: IRBuilder, cdef: ClassDef) -> None:
        super().__init__(builder, cdef)
        # If the class is not decorated, generate an extension class for it.
        self.type_obj: Optional[Value] = allocate_class(builder, cdef)

    def skip_attr_default(self, name: str, stmt: AssignmentStmt) -> bool:
        """Controls whether to skip generating a default for an attribute."""
        return False

    def add_method(self, fdef: FuncDef) -> None:
        handle_ext_method(self.builder, self.cdef, fdef)

    def add_attr(self, lvalue: NameExpr, stmt: AssignmentStmt) -> None:
        # Variable declaration with no body
        if isinstance(stmt.rvalue, TempNode):
            return
        # Only treat marked class variables as class variables.
        if not (is_class_var(lvalue) or stmt.is_final_def):
            return
        typ = self.builder.load_native_type_object(self.cdef.fullname)
        value = self.builder.accept(stmt.rvalue)
        self.builder.call_c(
            py_setattr_op, [typ, self.builder.load_str(lvalue.name), value], stmt.line)
        if self.builder.non_function_scope() and stmt.is_final_def:
            self.builder.init_final_static(lvalue, value, self.cdef.name)

    def finalize(self, ir: ClassIR) -> None:
        generate_attr_defaults(self.builder, self.cdef, self.skip_attr_default)
        create_ne_from_eq(self.builder, self.cdef)


class DataClassBuilder(ExtClassBuilder):
    # controls whether an __annotations__ attribute should be added to the class
    # __dict__.  This is not desirable for attrs classes where auto_attribs is
    # disabled, as attrs will reject it.
    add_annotations_to_dict = True

    def __init__(self, builder: IRBuilder, cdef: ClassDef) -> None:
        super().__init__(builder, cdef)
        self.non_ext = self.create_non_ext_info()

    def create_non_ext_info(self) -> NonExtClassInfo:
        """Set up a NonExtClassInfo to track dataclass attributes.

        In addition to setting up a normal extension class for dataclasses,
        we also collect its class attributes like a non-extension class so
        that we can hand them to the dataclass decorator.
        """
        return NonExtClassInfo(
            self.builder.call_c(dict_new_op, [], self.cdef.line),
            self.builder.add(TupleSet([], self.cdef.line)),
            self.builder.call_c(dict_new_op, [], self.cdef.line),
            self.builder.add(LoadAddress(type_object_op.type, type_object_op.src, self.cdef.line))
        )

    def skip_attr_default(self, name: str, stmt: AssignmentStmt) -> bool:
        return stmt.type is not None

    def get_type_annotation(self, stmt: AssignmentStmt) -> Optional[TypeInfo]:
        # We populate __annotations__ because dataclasses uses it to determine
        # which attributes to compute on.
        ann_type = get_proper_type(stmt.type)
        if isinstance(ann_type, Instance):
            return ann_type.type
        return None

    def add_attr(self, lvalue: NameExpr, stmt: AssignmentStmt) -> None:
        add_non_ext_class_attr_ann(self.builder, self.non_ext, lvalue, stmt,
                                   self.get_type_annotation)
        add_non_ext_class_attr(self.builder, self.non_ext, lvalue, stmt, self.cdef,
                               self.attrs_to_cache)
        super().add_attr(lvalue, stmt)

    def finalize(self, ir: ClassIR) -> None:
        """Generate code to finish instantiating a dataclass.

        This works by replacing all of the attributes on the class
        (which will be descriptors) with whatever they would be in a
        non-extension class, calling dataclass, then switching them back.

        The resulting class is an extension class and instances of it do not
        have a __dict__ (unless something else requires it).
        All methods written explicitly in the source are compiled and
        may be called through the vtable while the methods generated
        by dataclasses are interpreted and may not be.

        (If we just called dataclass without doing this, it would think that all
        of the descriptors for our attributes are default values and generate an
        incorrect constructor. We need to do the switch so that dataclass gets the
        appropriate defaults.)
        """
        super().finalize(ir)
        assert self.type_obj
        add_dunders_to_non_ext_dict(self.builder, self.non_ext, self.cdef.line,
                                    self.add_annotations_to_dict)
        dec = self.builder.accept(
            next(d for d in self.cdef.decorators if is_dataclass_decorator(d)))
        self.builder.call_c(
            dataclass_sleight_of_hand, [dec, self.type_obj, self.non_ext.dict, self.non_ext.anns],
            self.cdef.line)


class AttrsClassBuilder(DataClassBuilder):
    """Create IR for an attrs class where auto_attribs=False (the default).

    When auto_attribs is enabled, attrs classes behave similarly to dataclasses
    (i.e. types are stored as annotations on the class) and are thus handled
    by DataClassBuilder, but when auto_attribs is disabled the types are
    provided via attr.ib(type=...)
    """

    add_annotations_to_dict = False

    def skip_attr_default(self, name: str, stmt: AssignmentStmt) -> bool:
        return True

    def get_type_annotation(self, stmt: AssignmentStmt) -> Optional[TypeInfo]:
        if isinstance(stmt.rvalue, CallExpr):
            # find the type arg in `attr.ib(type=str)`
            callee = stmt.rvalue.callee
            if (isinstance(callee, MemberExpr) and
                    callee.fullname in ['attr.ib', 'attr.attr'] and
                    'type' in stmt.rvalue.arg_names):
                index = stmt.rvalue.arg_names.index('type')
                type_name = stmt.rvalue.args[index]
                if isinstance(type_name, NameExpr) and isinstance(type_name.node, TypeInfo):
                    lvalue = stmt.lvalues[0]
                    assert isinstance(lvalue, NameExpr)
                    return type_name.node
        return None


def allocate_class(builder: IRBuilder, cdef: ClassDef) -> Value:
    # OK AND NOW THE FUN PART
    base_exprs = cdef.base_type_exprs + cdef.removed_base_type_exprs
    if base_exprs:
        bases = [builder.accept(x) for x in base_exprs]
        tp_bases = builder.new_tuple(bases, cdef.line)
    else:
        tp_bases = builder.add(LoadErrorValue(object_rprimitive, is_borrowed=True))
    modname = builder.load_str(builder.module_name)
    template = builder.add(LoadStatic(object_rprimitive, cdef.name + "_template",
                                      builder.module_name, NAMESPACE_TYPE))
    # Create the class
    tp = builder.call_c(pytype_from_template_op,
                        [template, tp_bases, modname], cdef.line)
    # Immediately fix up the trait vtables, before doing anything with the class.
    ir = builder.mapper.type_to_ir[cdef.info]
    if not ir.is_trait and not ir.builtin_base:
        builder.add(Call(
            FuncDecl(cdef.name + '_trait_vtable_setup',
                     None, builder.module_name,
                     FuncSignature([], bool_rprimitive)), [], -1))
    # Populate a '__mypyc_attrs__' field containing the list of attrs
    builder.call_c(py_setattr_op, [
        tp, builder.load_str('__mypyc_attrs__'),
        create_mypyc_attrs_tuple(builder, builder.mapper.type_to_ir[cdef.info], cdef.line)],
        cdef.line)

    # Save the class
    builder.add(InitStatic(tp, cdef.name, builder.module_name, NAMESPACE_TYPE))

    # Add it to the dict
    builder.call_c(dict_set_item_op,
                   [builder.load_globals_dict(),
                    builder.load_str(cdef.name),
                    tp],
                   cdef.line)

    return tp


# Mypy uses these internally as base classes of TypedDict classes. These are
# lies and don't have any runtime equivalent.
MAGIC_TYPED_DICT_CLASSES: Final[Tuple[str, ...]] = (
    'typing._TypedDict',
    'typing_extensions._TypedDict',
)


def populate_non_ext_bases(builder: IRBuilder, cdef: ClassDef) -> Value:
    """Create base class tuple of a non-extension class.

    The tuple is passed to the metaclass constructor.
    """
    is_named_tuple = cdef.info.is_named_tuple
    ir = builder.mapper.type_to_ir[cdef.info]
    bases = []
    for cls in cdef.info.mro[1:]:
        if cls.fullname == 'builtins.object':
            continue
        if is_named_tuple and cls.fullname in ('typing.Sequence',
                                               'typing.Iterable',
                                               'typing.Collection',
                                               'typing.Reversible',
                                               'typing.Container'):
            # HAX: Synthesized base classes added by mypy don't exist at runtime, so skip them.
            #      This could break if they were added explicitly, though...
            continue
        # Add the current class to the base classes list of concrete subclasses
        if cls in builder.mapper.type_to_ir:
            base_ir = builder.mapper.type_to_ir[cls]
            if base_ir.children is not None:
                base_ir.children.append(ir)

        if cls.fullname in MAGIC_TYPED_DICT_CLASSES:
            # HAX: Mypy internally represents TypedDict classes differently from what
            #      should happen at runtime. Replace with something that works.
            module = 'typing'
            if builder.options.capi_version < (3, 9):
                name = 'TypedDict'
                if builder.options.capi_version < (3, 8):
                    # TypedDict was added to typing in Python 3.8.
                    module = 'typing_extensions'
            else:
                # In Python 3.9 TypedDict is not a real type.
                name = '_TypedDict'
            base = builder.get_module_attr(module, name, cdef.line)
        elif is_named_tuple and cls.fullname == 'builtins.tuple':
            if builder.options.capi_version < (3, 9):
                name = 'NamedTuple'
            else:
                # This was changed in Python 3.9.
                name = '_NamedTuple'
            base = builder.get_module_attr('typing', name, cdef.line)
        else:
            base = builder.load_global_str(cls.name, cdef.line)
        bases.append(base)
        if cls.fullname in MAGIC_TYPED_DICT_CLASSES:
            # The remaining base classes are synthesized by mypy and should be ignored.
            break
    return builder.new_tuple(bases, cdef.line)


def find_non_ext_metaclass(builder: IRBuilder, cdef: ClassDef, bases: Value) -> Value:
    """Find the metaclass of a class from its defs and bases. """
    if cdef.metaclass:
        declared_metaclass = builder.accept(cdef.metaclass)
    else:
        if cdef.info.typeddict_type is not None and builder.options.capi_version >= (3, 9):
            # In Python 3.9, the metaclass for class-based TypedDict is typing._TypedDictMeta.
            # We can't easily calculate it generically, so special case it.
            return builder.get_module_attr('typing', '_TypedDictMeta', cdef.line)
        elif cdef.info.is_named_tuple and builder.options.capi_version >= (3, 9):
            # In Python 3.9, the metaclass for class-based NamedTuple is typing.NamedTupleMeta.
            # We can't easily calculate it generically, so special case it.
            return builder.get_module_attr('typing', 'NamedTupleMeta', cdef.line)

        declared_metaclass = builder.add(LoadAddress(type_object_op.type,
                                                     type_object_op.src, cdef.line))

    return builder.call_c(py_calc_meta_op, [declared_metaclass, bases], cdef.line)


def setup_non_ext_dict(builder: IRBuilder,
                       cdef: ClassDef,
                       metaclass: Value,
                       bases: Value) -> Value:
    """Initialize the class dictionary for a non-extension class.

    This class dictionary is passed to the metaclass constructor.
    """
    # Check if the metaclass defines a __prepare__ method, and if so, call it.
    has_prepare = builder.call_c(py_hasattr_op,
                                 [metaclass,
                                  builder.load_str('__prepare__')], cdef.line)

    non_ext_dict = Register(dict_rprimitive)

    true_block, false_block, exit_block, = BasicBlock(), BasicBlock(), BasicBlock()
    builder.add_bool_branch(has_prepare, true_block, false_block)

    builder.activate_block(true_block)
    cls_name = builder.load_str(cdef.name)
    prepare_meth = builder.py_get_attr(metaclass, '__prepare__', cdef.line)
    prepare_dict = builder.py_call(prepare_meth, [cls_name, bases], cdef.line)
    builder.assign(non_ext_dict, prepare_dict, cdef.line)
    builder.goto(exit_block)

    builder.activate_block(false_block)
    builder.assign(non_ext_dict, builder.call_c(dict_new_op, [], cdef.line), cdef.line)
    builder.goto(exit_block)
    builder.activate_block(exit_block)

    return non_ext_dict


def add_non_ext_class_attr_ann(builder: IRBuilder,
                               non_ext: NonExtClassInfo,
                               lvalue: NameExpr,
                               stmt: AssignmentStmt,
                               get_type_info: Optional[Callable[[AssignmentStmt],
                                                                Optional[TypeInfo]]] = None
                               ) -> None:
    """Add a class attribute to __annotations__ of a non-extension class."""
    typ: Optional[Value] = None
    if get_type_info is not None:
        type_info = get_type_info(stmt)
        if type_info:
            typ = load_type(builder, type_info, stmt.line)

    if typ is None:
        # FIXME: if get_type_info is not provided, don't fall back to stmt.type?
        ann_type = get_proper_type(stmt.type)
        if isinstance(ann_type, Instance):
            typ = load_type(builder, ann_type.type, stmt.line)
        else:
            typ = builder.add(LoadAddress(type_object_op.type, type_object_op.src, stmt.line))

    key = builder.load_str(lvalue.name)
    builder.call_c(dict_set_item_op, [non_ext.anns, key, typ], stmt.line)


def add_non_ext_class_attr(builder: IRBuilder,
                           non_ext: NonExtClassInfo,
                           lvalue: NameExpr,
                           stmt: AssignmentStmt,
                           cdef: ClassDef,
                           attr_to_cache: List[Tuple[Lvalue, RType]]) -> None:
    """Add a class attribute to __dict__ of a non-extension class."""
    # Only add the attribute to the __dict__ if the assignment is of the form:
    # x: type = value (don't add attributes of the form 'x: type' to the __dict__).
    if not isinstance(stmt.rvalue, TempNode):
        rvalue = builder.accept(stmt.rvalue)
        builder.add_to_non_ext_dict(non_ext, lvalue.name, rvalue, stmt.line)
        # We cache enum attributes to speed up enum attribute lookup since they
        # are final.
        if (
            cdef.info.bases
            and cdef.info.bases[0].type.fullname == 'enum.Enum'
            # Skip these since Enum will remove it
            and lvalue.name not in ENUM_REMOVED_PROPS
        ):
            # Enum values are always boxed, so use object_rprimitive.
            attr_to_cache.append((lvalue, object_rprimitive))


def generate_attr_defaults(builder: IRBuilder, cdef: ClassDef,
                           skip: Optional[Callable[[str, AssignmentStmt], bool]] = None) -> None:
    """Generate an initialization method for default attr values (from class vars).

    If provided, the skip arg should be a callable which will return whether
    to skip generating a default for an attribute.  It will be passed the name of
    the attribute and the corresponding AssignmentStmt.
    """
    cls = builder.mapper.type_to_ir[cdef.info]
    if cls.builtin_base:
        return

    # Pull out all assignments in classes in the mro so we can initialize them
    # TODO: Support nested statements
    default_assignments = []
    for info in reversed(cdef.info.mro):
        if info not in builder.mapper.type_to_ir:
            continue
        for stmt in info.defn.defs.body:
            if (isinstance(stmt, AssignmentStmt)
                    and isinstance(stmt.lvalues[0], NameExpr)
                    and not is_class_var(stmt.lvalues[0])
                    and not isinstance(stmt.rvalue, TempNode)):
                name = stmt.lvalues[0].name
                if name == '__slots__':
                    continue

                if name == '__deletable__':
                    check_deletable_declaration(builder, cls, stmt.line)
                    continue

                if skip is not None and skip(name, stmt):
                    continue

                default_assignments.append(stmt)

    if not default_assignments:
        return

    with builder.enter_method(cls, '__mypyc_defaults_setup', bool_rprimitive):
        self_var = builder.self()
        for stmt in default_assignments:
            lvalue = stmt.lvalues[0]
            assert isinstance(lvalue, NameExpr)
            if not stmt.is_final_def and not is_constant(stmt.rvalue):
                builder.warning('Unsupported default attribute value', stmt.rvalue.line)

            # If the attribute is initialized to None and type isn't optional,
            # don't initialize it to anything.
            attr_type = cls.attr_type(lvalue.name)
            if isinstance(stmt.rvalue, RefExpr) and stmt.rvalue.fullname == 'builtins.None':
                if (not is_optional_type(attr_type) and not is_object_rprimitive(attr_type)
                        and not is_none_rprimitive(attr_type)):
                    continue
            val = builder.coerce(builder.accept(stmt.rvalue), attr_type, stmt.line)
            builder.add(SetAttr(self_var, lvalue.name, val, -1))

        builder.add(Return(builder.true()))


def check_deletable_declaration(builder: IRBuilder, cl: ClassIR, line: int) -> None:
    for attr in cl.deletable:
        if attr not in cl.attributes:
            if not cl.has_attr(attr):
                builder.error(f'Attribute "{attr}" not defined', line)
                continue
            for base in cl.mro:
                if attr in base.property_types:
                    builder.error(f'Cannot make property "{attr}" deletable', line)
                    break
            else:
                _, base = cl.attr_details(attr)
                builder.error(('Attribute "{}" not defined in "{}" ' +
                               '(defined in "{}")').format(attr, cl.name, base.name), line)


def create_ne_from_eq(builder: IRBuilder, cdef: ClassDef) -> None:
    """Create a "__ne__" method from a "__eq__" method (if only latter exists)."""
    cls = builder.mapper.type_to_ir[cdef.info]
    if cls.has_method('__eq__') and not cls.has_method('__ne__'):
        gen_glue_ne_method(builder, cls, cdef.line)


def gen_glue_ne_method(builder: IRBuilder, cls: ClassIR, line: int) -> None:
    """Generate a "__ne__" method from a "__eq__" method. """
    with builder.enter_method(cls, '__ne__', object_rprimitive):
        rhs_arg = builder.add_argument('rhs', object_rprimitive)

        # If __eq__ returns NotImplemented, then __ne__ should also
        not_implemented_block, regular_block = BasicBlock(), BasicBlock()
        eqval = builder.add(MethodCall(builder.self(), '__eq__', [rhs_arg], line))
        not_implemented = builder.add(LoadAddress(not_implemented_op.type,
                                                  not_implemented_op.src, line))
        builder.add(Branch(
            builder.translate_is_op(eqval, not_implemented, 'is', line),
            not_implemented_block,
            regular_block,
            Branch.BOOL))

        builder.activate_block(regular_block)
        retval = builder.coerce(
            builder.unary_op(eqval, 'not', line), object_rprimitive, line
        )
        builder.add(Return(retval))

        builder.activate_block(not_implemented_block)
        builder.add(Return(not_implemented))


def load_non_ext_class(builder: IRBuilder,
                       ir: ClassIR,
                       non_ext: NonExtClassInfo,
                       line: int) -> Value:
    cls_name = builder.load_str(ir.name)

    add_dunders_to_non_ext_dict(builder, non_ext, line)

    class_type_obj = builder.py_call(
        non_ext.metaclass,
        [cls_name, non_ext.bases, non_ext.dict],
        line
    )
    return class_type_obj


def load_decorated_class(builder: IRBuilder, cdef: ClassDef, type_obj: Value) -> Value:
    """Apply class decorators to create a decorated (non-extension) class object.

    Given a decorated ClassDef and a register containing a
    non-extension representation of the ClassDef created via the type
    constructor, applies the corresponding decorator functions on that
    decorated ClassDef and returns a register containing the decorated
    ClassDef.
    """
    decorators = cdef.decorators
    dec_class = type_obj
    for d in reversed(decorators):
        decorator = d.accept(builder.visitor)
        assert isinstance(decorator, Value)
        dec_class = builder.py_call(decorator, [dec_class], dec_class.line)
    return dec_class


def cache_class_attrs(builder: IRBuilder,
                      attrs_to_cache: List[Tuple[Lvalue, RType]],
                      cdef: ClassDef) -> None:
    """Add class attributes to be cached to the global cache."""
    typ = builder.load_native_type_object(cdef.info.fullname)
    for lval, rtype in attrs_to_cache:
        assert isinstance(lval, NameExpr)
        rval = builder.py_get_attr(typ, lval.name, cdef.line)
        builder.init_final_static(lval, rval, cdef.name, type_override=rtype)


def create_mypyc_attrs_tuple(builder: IRBuilder, ir: ClassIR, line: int) -> Value:
    attrs = [name for ancestor in ir.mro for name in ancestor.attributes]
    if ir.inherits_python:
        attrs.append('__dict__')
    items = [builder.load_str(attr) for attr in attrs]
    return builder.new_tuple(items, line)


def add_dunders_to_non_ext_dict(builder: IRBuilder, non_ext: NonExtClassInfo,
                                line: int, add_annotations: bool = True) -> None:
    if add_annotations:
        # Add __annotations__ to the class dict.
        builder.add_to_non_ext_dict(non_ext, '__annotations__', non_ext.anns, line)

    # We add a __doc__ attribute so if the non-extension class is decorated with the
    # dataclass decorator, dataclass will not try to look for __text_signature__.
    # https://github.com/python/cpython/blob/3.7/Lib/dataclasses.py#L957
    filler_doc_str = 'mypyc filler docstring'
    builder.add_to_non_ext_dict(
        non_ext, '__doc__', builder.load_str(filler_doc_str), line)
    builder.add_to_non_ext_dict(
        non_ext, '__module__', builder.load_str(builder.module_name), line)
