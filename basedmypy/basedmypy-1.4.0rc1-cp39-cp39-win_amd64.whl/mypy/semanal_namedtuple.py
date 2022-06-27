"""Semantic analysis of named tuple definitions.

This is conceptually part of mypy.semanal.
"""

from contextlib import contextmanager
from typing import Tuple, List, Dict, Mapping, Optional, Union, cast, Iterator
from typing_extensions import Final

from mypy.types import (
    Type, TupleType, AnyType, TypeOfAny, CallableType, TypeType, TypeVarType,
    UnboundType, LiteralType, UntypedType,
)
from mypy.semanal_shared import (
    SemanticAnalyzerInterface, set_callable_name, calculate_tuple_fallback, PRIORITY_FALLBACKS
)
from mypy.nodes import (
    Var, EllipsisExpr, Argument, StrExpr, BytesExpr, UnicodeExpr, ExpressionStmt, NameExpr,
    AssignmentStmt, PassStmt, Decorator, FuncBase, ClassDef, Expression, RefExpr, TypeInfo,
    NamedTupleExpr, CallExpr, Context, TupleExpr, ListExpr, SymbolTableNode, FuncDef, Block,
    TempNode, SymbolTable, TypeVarExpr, ARG_POS, ARG_NAMED_OPT, ARG_OPT, MDEF
)
from mypy.options import Options
from mypy.exprtotype import expr_to_unanalyzed_type, TypeTranslationError
from mypy.util import get_unique_redefinition_name

# Matches "_prohibited" in typing.py, but adds __annotations__, which works at runtime but can't
# easily be supported in a static checker.
NAMEDTUPLE_PROHIBITED_NAMES: Final = (
    "__new__",
    "__init__",
    "__slots__",
    "__getnewargs__",
    "_fields",
    "_field_defaults",
    "_field_types",
    "_make",
    "_replace",
    "_asdict",
    "_source",
    "__annotations__",
)

NAMEDTUP_CLASS_ERROR: Final = (
    "Invalid statement in NamedTuple definition; " 'expected "field_name: field_type [= default]"'
)

SELF_TVAR_NAME: Final = "_NT"


class NamedTupleAnalyzer:
    def __init__(self, options: Options, api: SemanticAnalyzerInterface) -> None:
        self.options = options
        self.api = api

    def analyze_namedtuple_classdef(self, defn: ClassDef, is_stub_file: bool,
                                    is_func_scope: bool
                                    ) -> Tuple[bool, Optional[TypeInfo]]:
        """Analyze if given class definition can be a named tuple definition.

        Return a tuple where first item indicates whether this can possibly be a named tuple,
        and the second item is the corresponding TypeInfo (may be None if not ready and should be
        deferred).
        """
        for base_expr in defn.base_type_exprs:
            if isinstance(base_expr, RefExpr):
                self.api.accept(base_expr)
                if base_expr.fullname == 'typing.NamedTuple':
                    result = self.check_namedtuple_classdef(defn, is_stub_file)
                    if result is None:
                        # This is a valid named tuple, but some types are incomplete.
                        return True, None
                    items, types, default_items = result
                    if is_func_scope and '@' not in defn.name:
                        defn.name += '@' + str(defn.line)
                    info = self.build_namedtuple_typeinfo(
                        defn.name, items, types, default_items, defn.line)
                    defn.info = info
                    defn.analyzed = NamedTupleExpr(info, is_typed=True)
                    defn.analyzed.line = defn.line
                    defn.analyzed.column = defn.column
                    # All done: this is a valid named tuple with all types known.
                    return True, info
        # This can't be a valid named tuple.
        return False, None

    def check_namedtuple_classdef(self, defn: ClassDef, is_stub_file: bool
                                  ) -> Optional[Tuple[List[str],
                                                List[Type],
                                                Dict[str, Expression]]]:
        """Parse and validate fields in named tuple class definition.

        Return a three tuple:
          * field names
          * field types
          * field default values
        or None, if any of the types are not ready.
        """
        if self.options.python_version < (3, 6) and not is_stub_file:
            self.fail('NamedTuple class syntax is only supported in Python 3.6', defn)
            return [], [], {}
        if len(defn.base_type_exprs) > 1:
            self.fail('NamedTuple should be a single base', defn)
        items: List[str] = []
        types: List[Type] = []
        default_items: Dict[str, Expression] = {}
        for stmt in defn.defs.body:
            if not isinstance(stmt, AssignmentStmt):
                # Still allow pass or ... (for empty namedtuples).
                if (isinstance(stmt, PassStmt) or
                    (isinstance(stmt, ExpressionStmt) and
                        isinstance(stmt.expr, EllipsisExpr))):
                    continue
                # Also allow methods, including decorated ones.
                if isinstance(stmt, (Decorator, FuncBase)):
                    continue
                # And docstrings.
                if (isinstance(stmt, ExpressionStmt) and
                        isinstance(stmt.expr, StrExpr)):
                    continue
                self.fail(NAMEDTUP_CLASS_ERROR, stmt)
            elif len(stmt.lvalues) > 1 or not isinstance(stmt.lvalues[0], NameExpr):
                # An assignment, but an invalid one.
                self.fail(NAMEDTUP_CLASS_ERROR, stmt)
            else:
                # Append name and type in this case...
                name = stmt.lvalues[0].name
                items.append(name)
                if stmt.type is None:
                    types.append(UntypedType())
                else:
                    analyzed = self.api.anal_type(stmt.type)
                    if analyzed is None:
                        # Something is incomplete. We need to defer this named tuple.
                        return None
                    types.append(analyzed)
                # ...despite possible minor failures that allow further analyzis.
                if name.startswith('_'):
                    self.fail('NamedTuple field name cannot start with an underscore: {}'
                              .format(name), stmt)
                if stmt.type is None or hasattr(stmt, 'new_syntax') and not stmt.new_syntax:
                    self.fail(NAMEDTUP_CLASS_ERROR, stmt)
                elif isinstance(stmt.rvalue, TempNode):
                    # x: int assigns rvalue to TempNode(AnyType())
                    if default_items:
                        self.fail('Non-default NamedTuple fields cannot follow default fields',
                                  stmt)
                else:
                    default_items[name] = stmt.rvalue
        return items, types, default_items

    def check_namedtuple(self,
                         node: Expression,
                         var_name: Optional[str],
                         is_func_scope: bool) -> Tuple[Optional[str], Optional[TypeInfo]]:
        """Check if a call defines a namedtuple.

        The optional var_name argument is the name of the variable to
        which this is assigned, if any.

        Return a tuple of two items:
          * Internal name of the named tuple (e.g. the name passed as an argument to namedtuple)
            or None if it is not a valid named tuple
          * Corresponding TypeInfo, or None if not ready.

        If the definition is invalid but looks like a namedtuple,
        report errors but return (some) TypeInfo.
        """
        if not isinstance(node, CallExpr):
            return None, None
        call = node
        callee = call.callee
        if not isinstance(callee, RefExpr):
            return None, None
        fullname = callee.fullname
        if fullname == 'collections.namedtuple':
            is_typed = False
        elif fullname == 'typing.NamedTuple':
            is_typed = True
        else:
            return None, None
        result = self.parse_namedtuple_args(call, fullname)
        if result:
            items, types, defaults, typename, ok = result
        else:
            # Error. Construct dummy return value.
            if var_name:
                name = var_name
                if is_func_scope:
                    name += '@' + str(call.line)
            else:
                name = var_name = 'namedtuple@' + str(call.line)
            info = self.build_namedtuple_typeinfo(name, [], [], {}, node.line)
            self.store_namedtuple_info(info, var_name, call, is_typed)
            if name != var_name or is_func_scope:
                # NOTE: we skip local namespaces since they are not serialized.
                self.api.add_symbol_skip_local(name, info)
            return var_name, info
        if not ok:
            # This is a valid named tuple but some types are not ready.
            return typename, None

        # We use the variable name as the class name if it exists. If
        # it doesn't, we use the name passed as an argument. We prefer
        # the variable name because it should be unique inside a
        # module, and so we don't need to disambiguate it with a line
        # number.
        if var_name:
            name = var_name
        else:
            name = typename

        if var_name is None or is_func_scope:
            # There are two special cases where need to give it a unique name derived
            # from the line number:
            #   * This is a base class expression, since it often matches the class name:
            #         class NT(NamedTuple('NT', [...])):
            #             ...
            #   * This is a local (function or method level) named tuple, since
            #     two methods of a class can define a named tuple with the same name,
            #     and they will be stored in the same namespace (see below).
            name += '@' + str(call.line)
        if len(defaults) > 0:
            default_items = {
                arg_name: default
                for arg_name, default in zip(items[-len(defaults):], defaults)
            }
        else:
            default_items = {}
        info = self.build_namedtuple_typeinfo(name, items, types, default_items, node.line)
        # If var_name is not None (i.e. this is not a base class expression), we always
        # store the generated TypeInfo under var_name in the current scope, so that
        # other definitions can use it.
        if var_name:
            self.store_namedtuple_info(info, var_name, call, is_typed)
        # There are three cases where we need to store the generated TypeInfo
        # second time (for the purpose of serialization):
        #   * If there is a name mismatch like One = NamedTuple('Other', [...])
        #     we also store the info under name 'Other@lineno', this is needed
        #     because classes are (de)serialized using their actual fullname, not
        #     the name of l.h.s.
        #   * If this is a method level named tuple. It can leak from the method
        #     via assignment to self attribute and therefore needs to be serialized
        #     (local namespaces are not serialized).
        #   * If it is a base class expression. It was not stored above, since
        #     there is no var_name (but it still needs to be serialized
        #     since it is in MRO of some class).
        if name != var_name or is_func_scope:
            # NOTE: we skip local namespaces since they are not serialized.
            self.api.add_symbol_skip_local(name, info)
        return typename, info

    def store_namedtuple_info(self, info: TypeInfo, name: str,
                              call: CallExpr, is_typed: bool) -> None:
        self.api.add_symbol(name, info, call)
        call.analyzed = NamedTupleExpr(info, is_typed=is_typed)
        call.analyzed.set_line(call.line, call.column)

    def parse_namedtuple_args(self, call: CallExpr, fullname: str
                              ) -> Optional[Tuple[List[str], List[Type], List[Expression],
                                            str, bool]]:
        """Parse a namedtuple() call into data needed to construct a type.

        Returns a 5-tuple:
        - List of argument names
        - List of argument types
        - List of default values
        - First argument of namedtuple
        - Whether all types are ready.

        Return None if the definition didn't typecheck.
        """
        type_name = 'NamedTuple' if fullname == 'typing.NamedTuple' else 'namedtuple'
        # TODO: Share code with check_argument_count in checkexpr.py?
        args = call.args
        if len(args) < 2:
            self.fail(f'Too few arguments for "{type_name}()"', call)
            return None
        defaults: List[Expression] = []
        if len(args) > 2:
            # Typed namedtuple doesn't support additional arguments.
            if fullname == 'typing.NamedTuple':
                self.fail('Too many arguments for "NamedTuple()"', call)
                return None
            for i, arg_name in enumerate(call.arg_names[2:], 2):
                if arg_name == 'defaults':
                    arg = args[i]
                    # We don't care what the values are, as long as the argument is an iterable
                    # and we can count how many defaults there are.
                    if isinstance(arg, (ListExpr, TupleExpr)):
                        defaults = list(arg.items)
                    else:
                        self.fail(
                            "List or tuple literal expected as the defaults argument to "
                            "{}()".format(type_name),
                            arg
                        )
                    break
        if call.arg_kinds[:2] != [ARG_POS, ARG_POS]:
            self.fail(f'Unexpected arguments to "{type_name}()"', call)
            return None
        if not isinstance(args[0], (StrExpr, BytesExpr, UnicodeExpr)):
            self.fail(
                f'"{type_name}()" expects a string literal as the first argument', call)
            return None
        typename = cast(Union[StrExpr, BytesExpr, UnicodeExpr], call.args[0]).value
        types: List[Type] = []
        if not isinstance(args[1], (ListExpr, TupleExpr)):
            if (fullname == 'collections.namedtuple'
                    and isinstance(args[1], (StrExpr, BytesExpr, UnicodeExpr))):
                str_expr = args[1]
                items = str_expr.value.replace(',', ' ').split()
            else:
                self.fail(
                    'List or tuple literal expected as the second argument to "{}()"'.format(
                        type_name,
                    ),
                    call,
                )
                return None
        else:
            listexpr = args[1]
            if fullname == 'collections.namedtuple':
                # The fields argument contains just names, with implicit Any types.
                if any(not isinstance(item, (StrExpr, BytesExpr, UnicodeExpr))
                       for item in listexpr.items):
                    self.fail('String literal expected as "namedtuple()" item', call)
                    return None
                items = [cast(Union[StrExpr, BytesExpr, UnicodeExpr], item).value
                         for item in listexpr.items]
            else:
                # The fields argument contains (name, type) tuples.
                result = self.parse_namedtuple_fields_with_types(listexpr.items, call)
                if result is None:
                    # One of the types is not ready, defer.
                    return None
                items, types, _, ok = result
                if not ok:
                    return [], [], [], typename, False
        if not types:
            types = [UntypedType() for _ in items]
        underscore = [item for item in items if item.startswith('_')]
        if underscore:
            self.fail(f'"{type_name}()" field names cannot start with an underscore: '
                      + ', '.join(underscore), call)
        if len(defaults) > len(items):
            self.fail(f'Too many defaults given in call to "{type_name}()"', call)
            defaults = defaults[:len(items)]
        return items, types, defaults, typename, True

    def parse_namedtuple_fields_with_types(self, nodes: List[Expression], context: Context
                                           ) -> Optional[Tuple[List[str], List[Type],
                                                               List[Expression], bool]]:
        """Parse typed named tuple fields.

        Return (names, types, defaults, whether types are all ready), or None if error occurred.
        """
        items: List[str] = []
        types: List[Type] = []
        for item in nodes:
            if isinstance(item, TupleExpr):
                if len(item.items) != 2:
                    self.fail('Invalid "NamedTuple()" field definition', item)
                    return None
                name, type_node = item.items
                if isinstance(name, (StrExpr, BytesExpr, UnicodeExpr)):
                    items.append(name.value)
                else:
                    self.fail('Invalid "NamedTuple()" field name', item)
                    return None
                try:
                    type = expr_to_unanalyzed_type(type_node, self.options, self.api.is_stub_file)
                except TypeTranslationError:
                    self.fail('Invalid field type', type_node)
                    return None
                analyzed = self.api.anal_type(type)
                # Workaround #4987 and avoid introducing a bogus UnboundType
                if isinstance(analyzed, UnboundType):
                    analyzed = AnyType(TypeOfAny.from_error)
                # These should be all known, otherwise we would defer in visit_assignment_stmt().
                if analyzed is None:
                    return [], [], [], False
                types.append(analyzed)
            else:
                self.fail('Tuple expected as "NamedTuple()" field', item)
                return None
        return items, types, [], True

    def build_namedtuple_typeinfo(self,
                                  name: str,
                                  items: List[str],
                                  types: List[Type],
                                  default_items: Mapping[str, Expression],
                                  line: int) -> TypeInfo:
        strtype = self.api.named_type('builtins.str')
        implicit_any = AnyType(TypeOfAny.special_form)
        basetuple_type = self.api.named_type('builtins.tuple', [implicit_any])
        dictype = (self.api.named_type_or_none('builtins.dict', [strtype, implicit_any])
                   or self.api.named_type('builtins.object'))
        # Actual signature should return OrderedDict[str, Union[types]]
        ordereddictype = (self.api.named_type_or_none('builtins.dict', [strtype, implicit_any])
                          or self.api.named_type('builtins.object'))
        fallback = self.api.named_type('builtins.tuple', [implicit_any])
        # Note: actual signature should accept an invariant version of Iterable[UnionType[types]].
        # but it can't be expressed. 'new' and 'len' should be callable types.
        iterable_type = self.api.named_type_or_none('typing.Iterable', [implicit_any])
        function_type = self.api.named_type('builtins.function')

        literals: List[Type] = [LiteralType(item, strtype) for item in items]
        match_args_type = TupleType(literals, basetuple_type)

        info = self.api.basic_new_typeinfo(name, fallback, line)
        info.is_named_tuple = True
        tuple_base = TupleType(types, fallback)
        info.tuple_type = tuple_base
        info.line = line
        # For use by mypyc.
        info.metadata['namedtuple'] = {'fields': items.copy()}

        # We can't calculate the complete fallback type until after semantic
        # analysis, since otherwise base classes might be incomplete. Postpone a
        # callback function that patches the fallback.
        self.api.schedule_patch(PRIORITY_FALLBACKS,
                                lambda: calculate_tuple_fallback(tuple_base))

        def add_field(var: Var, is_initialized_in_class: bool = False,
                      is_property: bool = False) -> None:
            var.info = info
            var.is_initialized_in_class = is_initialized_in_class
            var.is_property = is_property
            var._fullname = f'{info.fullname}.{var.name}'
            info.names[var.name] = SymbolTableNode(MDEF, var)

        fields = [Var(item, typ) for item, typ in zip(items, types)]
        for var in fields:
            add_field(var, is_property=True)
        # We can't share Vars between fields and method arguments, since they
        # have different full names (the latter are normally used as local variables
        # in functions, so their full names are set to short names when generated methods
        # are analyzed).
        vars = [Var(item, typ) for item, typ in zip(items, types)]

        tuple_of_strings = TupleType([strtype for _ in items], basetuple_type)
        add_field(Var('_fields', tuple_of_strings), is_initialized_in_class=True)
        add_field(Var('_field_types', dictype), is_initialized_in_class=True)
        add_field(Var('_field_defaults', dictype), is_initialized_in_class=True)
        add_field(Var('_source', strtype), is_initialized_in_class=True)
        add_field(Var('__annotations__', ordereddictype), is_initialized_in_class=True)
        add_field(Var('__doc__', strtype), is_initialized_in_class=True)
        add_field(Var('__match_args__', match_args_type), is_initialized_in_class=True)

        tvd = TypeVarType(SELF_TVAR_NAME, info.fullname + '.' + SELF_TVAR_NAME,
                         -1, [], info.tuple_type)
        selftype = tvd

        def add_method(funcname: str,
                       ret: Type,
                       args: List[Argument],
                       is_classmethod: bool = False,
                       is_new: bool = False,
                       ) -> None:
            if is_classmethod or is_new:
                first = [Argument(Var('_cls'), TypeType.make_normalized(selftype), None, ARG_POS)]
            else:
                first = [Argument(Var('_self'), selftype, None, ARG_POS)]
            args = first + args

            types = [arg.type_annotation for arg in args]
            items = [arg.variable.name for arg in args]
            arg_kinds = [arg.kind for arg in args]
            assert None not in types
            signature = CallableType(cast(List[Type], types), arg_kinds, items, ret,
                                     function_type)
            signature.variables = [tvd]
            func = FuncDef(funcname, args, Block([]))
            func.info = info
            func.is_class = is_classmethod
            func.type = set_callable_name(signature, func)
            func._fullname = info.fullname + '.' + funcname
            func.line = line
            if is_classmethod:
                v = Var(funcname, func.type)
                v.is_classmethod = True
                v.info = info
                v._fullname = func._fullname
                func.is_decorated = True
                dec = Decorator(func, [NameExpr('classmethod')], v)
                dec.line = line
                sym = SymbolTableNode(MDEF, dec)
            else:
                sym = SymbolTableNode(MDEF, func)
            sym.plugin_generated = True
            info.names[funcname] = sym

        add_method('_replace', ret=selftype,
                   args=[Argument(var, var.type, EllipsisExpr(), ARG_NAMED_OPT) for var in vars])

        def make_init_arg(var: Var) -> Argument:
            default = default_items.get(var.name, None)
            kind = ARG_POS if default is None else ARG_OPT
            return Argument(var, var.type, default, kind)

        add_method('__new__', ret=selftype,
                   args=[make_init_arg(var) for var in vars],
                   is_new=True)
        add_method('_asdict', args=[], ret=ordereddictype)
        special_form_any = AnyType(TypeOfAny.special_form)
        add_method('_make', ret=selftype, is_classmethod=True,
                   args=[Argument(Var('iterable', iterable_type), iterable_type, None, ARG_POS),
                         Argument(Var('new'), special_form_any, EllipsisExpr(), ARG_NAMED_OPT),
                         Argument(Var('len'), special_form_any, EllipsisExpr(), ARG_NAMED_OPT)])

        self_tvar_expr = TypeVarExpr(SELF_TVAR_NAME, info.fullname + '.' + SELF_TVAR_NAME,
                                     [], info.tuple_type)
        info.names[SELF_TVAR_NAME] = SymbolTableNode(MDEF, self_tvar_expr)
        return info

    @contextmanager
    def save_namedtuple_body(self, named_tuple_info: TypeInfo) -> Iterator[None]:
        """Preserve the generated body of class-based named tuple and then restore it.

        Temporarily clear the names dict so we don't get errors about duplicate names
        that were already set in build_namedtuple_typeinfo (we already added the tuple
        field names while generating the TypeInfo, and actual duplicates are
        already reported).
        """
        nt_names = named_tuple_info.names
        named_tuple_info.names = SymbolTable()

        yield

        # Make sure we didn't use illegal names, then reset the names in the typeinfo.
        for prohibited in NAMEDTUPLE_PROHIBITED_NAMES:
            if prohibited in named_tuple_info.names:
                if nt_names.get(prohibited) is named_tuple_info.names[prohibited]:
                    continue
                ctx = named_tuple_info.names[prohibited].node
                assert ctx is not None
                self.fail(f'Cannot overwrite NamedTuple attribute "{prohibited}"',
                          ctx)

        # Restore the names in the original symbol table. This ensures that the symbol
        # table contains the field objects created by build_namedtuple_typeinfo. Exclude
        # __doc__, which can legally be overwritten by the class.
        for key, value in nt_names.items():
            if key in named_tuple_info.names:
                if key == '__doc__':
                    continue
                sym = named_tuple_info.names[key]
                if isinstance(sym.node, (FuncBase, Decorator)) and not sym.plugin_generated:
                    # Keep user-defined methods as is.
                    continue
                # Keep existing (user-provided) definitions under mangled names, so they
                # get semantically analyzed.
                r_key = get_unique_redefinition_name(key, named_tuple_info.names)
                named_tuple_info.names[r_key] = sym
            named_tuple_info.names[key] = value

    # Helpers

    def fail(self, msg: str, ctx: Context) -> None:
        self.api.fail(msg, ctx)
