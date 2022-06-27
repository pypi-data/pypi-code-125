"""Transform mypy AST functions to IR (and related things).

Normal functions are translated into a list of basic blocks
containing various IR ops (defined in mypyc.ir.ops).

This also deals with generators, async functions and nested
functions. All of these are transformed into callable classes. These
have a custom __call__ method that implements the call, and state, such
as an environment containing non-local variables, is stored in the
instance of the callable class.
"""

from typing import (
    DefaultDict, NamedTuple, Optional, List, Sequence, Tuple, Union, Dict,
)

from mypy.nodes import (
    ClassDef, FuncDef, OverloadedFuncDef, Decorator, Var, YieldFromExpr, AwaitExpr, YieldExpr,
    FuncItem, LambdaExpr, SymbolNode, ArgKind, TypeInfo
)
from mypy.types import CallableType, get_proper_type

from mypyc.ir.ops import (
    BasicBlock, Value,  Register, Return, SetAttr, Integer, GetAttr, Branch, InitStatic,
    LoadAddress, LoadLiteral, Unbox, Unreachable,
)
from mypyc.ir.rtypes import (
    object_rprimitive, RInstance, object_pointer_rprimitive, dict_rprimitive, int_rprimitive,
    bool_rprimitive,
)
from mypyc.ir.func_ir import (
    FuncIR, FuncSignature, RuntimeArg, FuncDecl, FUNC_CLASSMETHOD, FUNC_STATICMETHOD, FUNC_NORMAL
)
from mypyc.ir.class_ir import ClassIR, NonExtClassInfo
from mypyc.primitives.generic_ops import py_setattr_op, next_raw_op, iter_op
from mypyc.primitives.misc_ops import (
    check_stop_op, yield_from_except_op, coro_op, send_op, register_function
)
from mypyc.primitives.dict_ops import dict_set_item_op, dict_new_op, dict_get_method_with_none
from mypyc.common import SELF_NAME, LAMBDA_NAME
from mypyc.sametype import is_same_method_signature
from mypyc.irbuild.util import is_constant
from mypyc.irbuild.context import FuncInfo, ImplicitClass
from mypyc.irbuild.targets import AssignmentTarget
from mypyc.irbuild.statement import transform_try_except
from mypyc.irbuild.builder import IRBuilder, SymbolTarget, gen_arg_defaults
from mypyc.irbuild.callable_class import (
    setup_callable_class, add_call_to_callable_class, add_get_to_callable_class,
    instantiate_callable_class
)
from mypyc.irbuild.generator import (
    gen_generator_func, setup_env_for_generator_class, create_switch_for_generator_class,
    add_raise_exception_blocks_to_generator_class, populate_switch_for_generator_class,
    add_methods_to_generator_class
)
from mypyc.irbuild.env_class import (
    setup_env_class, load_outer_envs, load_env_registers, finalize_env_class,
    setup_func_for_recursive_call
)

from mypyc.primitives.registry import builtin_names
from collections import defaultdict


# Top-level transform functions


def transform_func_def(builder: IRBuilder, fdef: FuncDef) -> None:
    func_ir, func_reg = gen_func_item(builder, fdef, fdef.name, builder.mapper.fdef_to_sig(fdef))

    # If the function that was visited was a nested function, then either look it up in our
    # current environment or define it if it was not already defined.
    if func_reg:
        builder.assign(get_func_target(builder, fdef), func_reg, fdef.line)
    maybe_insert_into_registry_dict(builder, fdef)
    builder.functions.append(func_ir)


def transform_overloaded_func_def(builder: IRBuilder, o: OverloadedFuncDef) -> None:
    # Handle regular overload case
    assert o.impl
    builder.accept(o.impl)


def transform_decorator(builder: IRBuilder, dec: Decorator) -> None:
    func_ir, func_reg = gen_func_item(
        builder,
        dec.func,
        dec.func.name,
        builder.mapper.fdef_to_sig(dec.func)
    )
    decorated_func: Optional[Value] = None
    if func_reg:
        decorated_func = load_decorated_func(builder, dec.func, func_reg)
        builder.assign(get_func_target(builder, dec.func), decorated_func, dec.func.line)
        func_reg = decorated_func
    # If the prebuild pass didn't put this function in the function to decorators map (for example
    # if this is a registered singledispatch implementation with no other decorators), we should
    # treat this function as a regular function, not a decorated function
    elif dec.func in builder.fdefs_to_decorators:
        # Obtain the the function name in order to construct the name of the helper function.
        name = dec.func.fullname.split('.')[-1]

        # Load the callable object representing the non-decorated function, and decorate it.
        orig_func = builder.load_global_str(name, dec.line)
        decorated_func = load_decorated_func(builder, dec.func, orig_func)

    if decorated_func is not None:
        # Set the callable object representing the decorated function as a global.
        builder.call_c(dict_set_item_op,
                       [builder.load_globals_dict(),
                        builder.load_str(dec.func.name), decorated_func],
                       decorated_func.line)

    maybe_insert_into_registry_dict(builder, dec.func)

    builder.functions.append(func_ir)


def transform_lambda_expr(builder: IRBuilder, expr: LambdaExpr) -> Value:
    typ = get_proper_type(builder.types[expr])
    assert isinstance(typ, CallableType)

    runtime_args = []
    for arg, arg_type in zip(expr.arguments, typ.arg_types):
        arg.variable.type = arg_type
        runtime_args.append(
            RuntimeArg(arg.variable.name, builder.type_to_rtype(arg_type), arg.kind))
    ret_type = builder.type_to_rtype(typ.ret_type)

    fsig = FuncSignature(runtime_args, ret_type)

    fname = f'{LAMBDA_NAME}{builder.lambda_counter}'
    builder.lambda_counter += 1
    func_ir, func_reg = gen_func_item(builder, expr, fname, fsig)
    assert func_reg is not None

    builder.functions.append(func_ir)
    return func_reg


def transform_yield_expr(builder: IRBuilder, expr: YieldExpr) -> Value:
    if builder.fn_info.is_coroutine:
        builder.error('async generators are unimplemented', expr.line)

    if expr.expr:
        retval = builder.accept(expr.expr)
    else:
        retval = builder.builder.none()
    return emit_yield(builder, retval, expr.line)


def transform_yield_from_expr(builder: IRBuilder, o: YieldFromExpr) -> Value:
    return handle_yield_from_and_await(builder, o)


def transform_await_expr(builder: IRBuilder, o: AwaitExpr) -> Value:
    return handle_yield_from_and_await(builder, o)


# Internal functions


def gen_func_item(builder: IRBuilder,
                  fitem: FuncItem,
                  name: str,
                  sig: FuncSignature,
                  cdef: Optional[ClassDef] = None,
                  ) -> Tuple[FuncIR, Optional[Value]]:
    """Generate and return the FuncIR for a given FuncDef.

    If the given FuncItem is a nested function, then we generate a
    callable class representing the function and use that instead of
    the actual function. if the given FuncItem contains a nested
    function, then we generate an environment class so that inner
    nested functions can access the environment of the given FuncDef.

    Consider the following nested function:

        def a() -> None:
            def b() -> None:
                def c() -> None:
                    return None
                return None
            return None

    The classes generated would look something like the following.

                has pointer to        +-------+
        +-------------------------->  | a_env |
        |                             +-------+
        |                                 ^
        |                                 | has pointer to
    +-------+     associated with     +-------+
    | b_obj |   ------------------->  | b_env |
    +-------+                         +-------+
                                          ^
                                          |
    +-------+         has pointer to      |
    | c_obj |   --------------------------+
    +-------+
    """

    # TODO: do something about abstract methods.

    func_reg: Optional[Value] = None

    # We treat lambdas as always being nested because we always generate
    # a class for lambdas, no matter where they are. (It would probably also
    # work to special case toplevel lambdas and generate a non-class function.)
    is_nested = fitem in builder.nested_fitems or isinstance(fitem, LambdaExpr)
    contains_nested = fitem in builder.encapsulating_funcs.keys()
    is_decorated = fitem in builder.fdefs_to_decorators
    is_singledispatch = fitem in builder.singledispatch_impls
    in_non_ext = False
    class_name = None
    if cdef:
        ir = builder.mapper.type_to_ir[cdef.info]
        in_non_ext = not ir.is_ext_class
        class_name = cdef.name

    if is_singledispatch:
        func_name = singledispatch_main_func_name(name)
    else:
        func_name = name
    builder.enter(FuncInfo(fitem, func_name, class_name, gen_func_ns(builder),
                           is_nested, contains_nested, is_decorated, in_non_ext))

    # Functions that contain nested functions need an environment class to store variables that
    # are free in their nested functions. Generator functions need an environment class to
    # store a variable denoting the next instruction to be executed when the __next__ function
    # is called, along with all the variables inside the function itself.
    if builder.fn_info.contains_nested or builder.fn_info.is_generator:
        setup_env_class(builder)

    if builder.fn_info.is_nested or builder.fn_info.in_non_ext:
        setup_callable_class(builder)

    if builder.fn_info.is_generator:
        # Do a first-pass and generate a function that just returns a generator object.
        gen_generator_func(builder)
        args, _, blocks, ret_type, fn_info = builder.leave()
        func_ir, func_reg = gen_func_ir(
            builder, args, blocks, sig, fn_info, cdef, is_singledispatch,
        )

        # Re-enter the FuncItem and visit the body of the function this time.
        builder.enter(fn_info)
        setup_env_for_generator_class(builder)
        load_outer_envs(builder, builder.fn_info.generator_class)
        if builder.fn_info.is_nested and isinstance(fitem, FuncDef):
            setup_func_for_recursive_call(builder, fitem, builder.fn_info.generator_class)
        create_switch_for_generator_class(builder)
        add_raise_exception_blocks_to_generator_class(builder, fitem.line)
    else:
        load_env_registers(builder)
        gen_arg_defaults(builder)

    if builder.fn_info.contains_nested and not builder.fn_info.is_generator:
        finalize_env_class(builder)

    builder.ret_types[-1] = sig.ret_type

    # Add all variables and functions that are declared/defined within this
    # function and are referenced in functions nested within this one to this
    # function's environment class so the nested functions can reference
    # them even if they are declared after the nested function's definition.
    # Note that this is done before visiting the body of this function.

    env_for_func: Union[FuncInfo, ImplicitClass] = builder.fn_info
    if builder.fn_info.is_generator:
        env_for_func = builder.fn_info.generator_class
    elif builder.fn_info.is_nested or builder.fn_info.in_non_ext:
        env_for_func = builder.fn_info.callable_class

    if builder.fn_info.fitem in builder.free_variables:
        # Sort the variables to keep things deterministic
        for var in sorted(builder.free_variables[builder.fn_info.fitem],
                          key=lambda x: x.name):
            if isinstance(var, Var):
                rtype = builder.type_to_rtype(var.type)
                builder.add_var_to_env_class(var, rtype, env_for_func, reassign=False)

    if builder.fn_info.fitem in builder.encapsulating_funcs:
        for nested_fn in builder.encapsulating_funcs[builder.fn_info.fitem]:
            if isinstance(nested_fn, FuncDef):
                # The return type is 'object' instead of an RInstance of the
                # callable class because differently defined functions with
                # the same name and signature across conditional blocks
                # will generate different callable classes, so the callable
                # class that gets instantiated must be generic.
                builder.add_var_to_env_class(
                    nested_fn, object_rprimitive, env_for_func, reassign=False
                )

    builder.accept(fitem.body)
    builder.maybe_add_implicit_return()

    if builder.fn_info.is_generator:
        populate_switch_for_generator_class(builder)

    # Hang on to the local symbol table for a while, since we use it
    # to calculate argument defaults below.
    symtable = builder.symtables[-1]

    args, _, blocks, ret_type, fn_info = builder.leave()

    if fn_info.is_generator:
        add_methods_to_generator_class(
            builder, fn_info, sig, args, blocks, fitem.is_coroutine)
    else:
        func_ir, func_reg = gen_func_ir(
            builder, args, blocks, sig, fn_info, cdef, is_singledispatch,
        )

    # Evaluate argument defaults in the surrounding scope, since we
    # calculate them *once* when the function definition is evaluated.
    calculate_arg_defaults(builder, fn_info, func_reg, symtable)

    if is_singledispatch:
        # add the generated main singledispatch function
        builder.functions.append(func_ir)
        # create the dispatch function
        assert isinstance(fitem, FuncDef)
        return gen_dispatch_func_ir(builder, fitem, fn_info.name, name, sig)

    return func_ir, func_reg


def gen_func_ir(builder: IRBuilder,
                args: List[Register],
                blocks: List[BasicBlock],
                sig: FuncSignature,
                fn_info: FuncInfo,
                cdef: Optional[ClassDef],
                is_singledispatch_main_func: bool = False) -> Tuple[FuncIR, Optional[Value]]:
    """Generate the FuncIR for a function.

    This takes the basic blocks and function info of a particular
    function and returns the IR. If the function is nested,
    also returns the register containing the instance of the
    corresponding callable class.
    """
    func_reg: Optional[Value] = None
    if fn_info.is_nested or fn_info.in_non_ext:
        func_ir = add_call_to_callable_class(builder, args, blocks, sig, fn_info)
        add_get_to_callable_class(builder, fn_info)
        func_reg = instantiate_callable_class(builder, fn_info)
    else:
        assert isinstance(fn_info.fitem, FuncDef)
        func_decl = builder.mapper.func_to_decl[fn_info.fitem]
        if fn_info.is_decorated or is_singledispatch_main_func:
            class_name = None if cdef is None else cdef.name
            func_decl = FuncDecl(fn_info.name, class_name, builder.module_name, sig,
                                 func_decl.kind,
                                 func_decl.is_prop_getter, func_decl.is_prop_setter)
            func_ir = FuncIR(func_decl, args, blocks, fn_info.fitem.line,
                             traceback_name=fn_info.fitem.name)
        else:
            func_ir = FuncIR(func_decl, args, blocks,
                             fn_info.fitem.line, traceback_name=fn_info.fitem.name)
    return (func_ir, func_reg)


def handle_ext_method(builder: IRBuilder, cdef: ClassDef, fdef: FuncDef) -> None:
    # Perform the function of visit_method for methods inside extension classes.
    name = fdef.name
    class_ir = builder.mapper.type_to_ir[cdef.info]
    func_ir, func_reg = gen_func_item(builder, fdef, name, builder.mapper.fdef_to_sig(fdef), cdef)
    builder.functions.append(func_ir)

    if is_decorated(builder, fdef):
        # Obtain the the function name in order to construct the name of the helper function.
        _, _, name = fdef.fullname.rpartition('.')
        # Read the PyTypeObject representing the class, get the callable object
        # representing the non-decorated method
        typ = builder.load_native_type_object(cdef.fullname)
        orig_func = builder.py_get_attr(typ, name, fdef.line)

        # Decorate the non-decorated method
        decorated_func = load_decorated_func(builder, fdef, orig_func)

        # Set the callable object representing the decorated method as an attribute of the
        # extension class.
        builder.call_c(py_setattr_op,
                       [typ, builder.load_str(name), decorated_func],
                       fdef.line)

    if fdef.is_property:
        # If there is a property setter, it will be processed after the getter,
        # We populate the optional setter field with none for now.
        assert name not in class_ir.properties
        class_ir.properties[name] = (func_ir, None)

    elif fdef in builder.prop_setters:
        # The respective property getter must have been processed already
        assert name in class_ir.properties
        getter_ir, _ = class_ir.properties[name]
        class_ir.properties[name] = (getter_ir, func_ir)

    class_ir.methods[func_ir.decl.name] = func_ir

    # If this overrides a parent class method with a different type, we need
    # to generate a glue method to mediate between them.
    for base in class_ir.mro[1:]:
        if (name in base.method_decls and name != '__init__'
                and not is_same_method_signature(class_ir.method_decls[name].sig,
                                                 base.method_decls[name].sig)):

            # TODO: Support contravariant subtyping in the input argument for
            # property setters. Need to make a special glue method for handling this,
            # similar to gen_glue_property.

            f = gen_glue(builder, base.method_decls[name].sig, func_ir, class_ir, base, fdef)
            class_ir.glue_methods[(base, name)] = f
            builder.functions.append(f)

    # If the class allows interpreted children, create glue
    # methods that dispatch via the Python API. These will go in a
    # "shadow vtable" that will be assigned to interpreted
    # children.
    if class_ir.allow_interpreted_subclasses:
        f = gen_glue(builder, func_ir.sig, func_ir, class_ir, class_ir, fdef, do_py_ops=True)
        class_ir.glue_methods[(class_ir, name)] = f
        builder.functions.append(f)


def handle_non_ext_method(
        builder: IRBuilder, non_ext: NonExtClassInfo, cdef: ClassDef, fdef: FuncDef) -> None:
    # Perform the function of visit_method for methods inside non-extension classes.
    name = fdef.name
    func_ir, func_reg = gen_func_item(builder, fdef, name, builder.mapper.fdef_to_sig(fdef), cdef)
    assert func_reg is not None
    builder.functions.append(func_ir)

    if is_decorated(builder, fdef):
        # The undecorated method is a generated callable class
        orig_func = func_reg
        func_reg = load_decorated_func(builder, fdef, orig_func)

    # TODO: Support property setters in non-extension classes
    if fdef.is_property:
        prop = builder.load_module_attr_by_fullname('builtins.property', fdef.line)
        func_reg = builder.py_call(prop, [func_reg], fdef.line)

    elif builder.mapper.func_to_decl[fdef].kind == FUNC_CLASSMETHOD:
        cls_meth = builder.load_module_attr_by_fullname('builtins.classmethod', fdef.line)
        func_reg = builder.py_call(cls_meth, [func_reg], fdef.line)

    elif builder.mapper.func_to_decl[fdef].kind == FUNC_STATICMETHOD:
        stat_meth = builder.load_module_attr_by_fullname(
            'builtins.staticmethod', fdef.line
        )
        func_reg = builder.py_call(stat_meth, [func_reg], fdef.line)

    builder.add_to_non_ext_dict(non_ext, name, func_reg, fdef.line)


def calculate_arg_defaults(builder: IRBuilder,
                           fn_info: FuncInfo,
                           func_reg: Optional[Value],
                           symtable: Dict[SymbolNode, SymbolTarget]) -> None:
    """Calculate default argument values and store them.

    They are stored in statics for top level functions and in
    the function objects for nested functions (while constants are
    still stored computed on demand).
    """
    fitem = fn_info.fitem
    for arg in fitem.arguments:
        # Constant values don't get stored but just recomputed
        if arg.initializer and not is_constant(arg.initializer):
            value = builder.coerce(
                builder.accept(arg.initializer),
                symtable[arg.variable].type,
                arg.line
            )
            if not fn_info.is_nested:
                name = fitem.fullname + '.' + arg.variable.name
                builder.add(InitStatic(value, name, builder.module_name))
            else:
                assert func_reg is not None
                builder.add(SetAttr(func_reg, arg.variable.name, value, arg.line))


def gen_func_ns(builder: IRBuilder) -> str:
    """Generate a namespace for a nested function using its outer function names."""
    return '_'.join(info.name + ('' if not info.class_name else '_' + info.class_name)
                    for info in builder.fn_infos
                    if info.name and info.name != '<top level>')


def emit_yield(builder: IRBuilder, val: Value, line: int) -> Value:
    retval = builder.coerce(val, builder.ret_types[-1], line)

    cls = builder.fn_info.generator_class
    # Create a new block for the instructions immediately following the yield expression, and
    # set the next label so that the next time '__next__' is called on the generator object,
    # the function continues at the new block.
    next_block = BasicBlock()
    next_label = len(cls.continuation_blocks)
    cls.continuation_blocks.append(next_block)
    builder.assign(cls.next_label_target, Integer(next_label), line)
    builder.add(Return(retval))
    builder.activate_block(next_block)

    add_raise_exception_blocks_to_generator_class(builder, line)

    assert cls.send_arg_reg is not None
    return cls.send_arg_reg


def handle_yield_from_and_await(builder: IRBuilder, o: Union[YieldFromExpr, AwaitExpr]) -> Value:
    # This is basically an implementation of the code in PEP 380.

    # TODO: do we want to use the right types here?
    result = Register(object_rprimitive)
    to_yield_reg = Register(object_rprimitive)
    received_reg = Register(object_rprimitive)

    if isinstance(o, YieldFromExpr):
        iter_val = builder.call_c(iter_op, [builder.accept(o.expr)], o.line)
    else:
        iter_val = builder.call_c(coro_op, [builder.accept(o.expr)], o.line)

    iter_reg = builder.maybe_spill_assignable(iter_val)

    stop_block, main_block, done_block = BasicBlock(), BasicBlock(), BasicBlock()
    _y_init = builder.call_c(next_raw_op, [builder.read(iter_reg)], o.line)
    builder.add(Branch(_y_init, stop_block, main_block, Branch.IS_ERROR))

    # Try extracting a return value from a StopIteration and return it.
    # If it wasn't, this reraises the exception.
    builder.activate_block(stop_block)
    builder.assign(result, builder.call_c(check_stop_op, [], o.line), o.line)
    builder.goto(done_block)

    builder.activate_block(main_block)
    builder.assign(to_yield_reg, _y_init, o.line)

    # OK Now the main loop!
    loop_block = BasicBlock()
    builder.goto_and_activate(loop_block)

    def try_body() -> None:
        builder.assign(
            received_reg, emit_yield(builder, builder.read(to_yield_reg), o.line), o.line
        )

    def except_body() -> None:
        # The body of the except is all implemented in a C function to
        # reduce how much code we need to generate. It returns a value
        # indicating whether to break or yield (or raise an exception).
        val = Register(object_rprimitive)
        val_address = builder.add(LoadAddress(object_pointer_rprimitive, val))
        to_stop = builder.call_c(yield_from_except_op,
                                 [builder.read(iter_reg), val_address], o.line)

        ok, stop = BasicBlock(), BasicBlock()
        builder.add(Branch(to_stop, stop, ok, Branch.BOOL))

        # The exception got swallowed. Continue, yielding the returned value
        builder.activate_block(ok)
        builder.assign(to_yield_reg, val, o.line)
        builder.nonlocal_control[-1].gen_continue(builder, o.line)

        # The exception was a StopIteration. Stop iterating.
        builder.activate_block(stop)
        builder.assign(result, val, o.line)
        builder.nonlocal_control[-1].gen_break(builder, o.line)

    def else_body() -> None:
        # Do a next() or a .send(). It will return NULL on exception
        # but it won't automatically propagate.
        _y = builder.call_c(
            send_op, [builder.read(iter_reg), builder.read(received_reg)], o.line
        )
        ok, stop = BasicBlock(), BasicBlock()
        builder.add(Branch(_y, stop, ok, Branch.IS_ERROR))

        # Everything's fine. Yield it.
        builder.activate_block(ok)
        builder.assign(to_yield_reg, _y, o.line)
        builder.nonlocal_control[-1].gen_continue(builder, o.line)

        # Try extracting a return value from a StopIteration and return it.
        # If it wasn't, this rereaises the exception.
        builder.activate_block(stop)
        builder.assign(result, builder.call_c(check_stop_op, [], o.line), o.line)
        builder.nonlocal_control[-1].gen_break(builder, o.line)

    builder.push_loop_stack(loop_block, done_block)
    transform_try_except(
        builder, try_body, [(None, None, except_body)], else_body, o.line
    )
    builder.pop_loop_stack()

    builder.goto_and_activate(done_block)
    return builder.read(result)


def load_decorated_func(builder: IRBuilder, fdef: FuncDef, orig_func_reg: Value) -> Value:
    """Apply decorators to a function.

    Given a decorated FuncDef and an instance of the callable class
    representing that FuncDef, apply the corresponding decorator
    functions on that decorated FuncDef and return the decorated
    function.
    """
    if not is_decorated(builder, fdef):
        # If there are no decorators associated with the function, then just return the
        # original function.
        return orig_func_reg

    decorators = builder.fdefs_to_decorators[fdef]
    func_reg = orig_func_reg
    for d in reversed(decorators):
        decorator = d.accept(builder.visitor)
        assert isinstance(decorator, Value)
        func_reg = builder.py_call(decorator, [func_reg], func_reg.line)
    return func_reg


def is_decorated(builder: IRBuilder, fdef: FuncDef) -> bool:
    return fdef in builder.fdefs_to_decorators


def gen_glue(builder: IRBuilder, sig: FuncSignature, target: FuncIR,
             cls: ClassIR, base: ClassIR, fdef: FuncItem,
             *,
             do_py_ops: bool = False
             ) -> FuncIR:
    """Generate glue methods that mediate between different method types in subclasses.

    Works on both properties and methods. See gen_glue_methods below
    for more details.

    If do_py_ops is True, then the glue methods should use generic
    C API operations instead of direct calls, to enable generating
    "shadow" glue methods that work with interpreted subclasses.
    """
    if fdef.is_property:
        return gen_glue_property(builder, sig, target, cls, base, fdef.line, do_py_ops)
    else:
        return gen_glue_method(builder, sig, target, cls, base, fdef.line, do_py_ops)


class ArgInfo(NamedTuple):
    args: List[Value]
    arg_names: List[Optional[str]]
    arg_kinds: List[ArgKind]


def get_args(builder: IRBuilder, rt_args: Sequence[RuntimeArg], line: int) -> ArgInfo:
    # The environment operates on Vars, so we make some up
    fake_vars = [(Var(arg.name), arg.type) for arg in rt_args]
    args = [builder.read(builder.add_local_reg(var, type, is_arg=True), line)
            for var, type in fake_vars]
    arg_names = [arg.name
                 if arg.kind.is_named() or (arg.kind.is_optional() and not arg.pos_only) else None
                 for arg in rt_args]
    arg_kinds = [arg.kind for arg in rt_args]
    return ArgInfo(args, arg_names, arg_kinds)


def gen_glue_method(builder: IRBuilder, sig: FuncSignature, target: FuncIR,
                    cls: ClassIR, base: ClassIR, line: int,
                    do_pycall: bool,
                    ) -> FuncIR:
    """Generate glue methods that mediate between different method types in subclasses.

    For example, if we have:

    class A:
        def f(builder: IRBuilder, x: int) -> object: ...

    then it is totally permissible to have a subclass

    class B(A):
        def f(builder: IRBuilder, x: object) -> int: ...

    since '(object) -> int' is a subtype of '(int) -> object' by the usual
    contra/co-variant function subtyping rules.

    The trickiness here is that int and object have different
    runtime representations in mypyc, so A.f and B.f have
    different signatures at the native C level. To deal with this,
    we need to generate glue methods that mediate between the
    different versions by coercing the arguments and return
    values.

    If do_pycall is True, then make the call using the C API
    instead of a native call.
    """
    builder.enter()
    builder.ret_types[-1] = sig.ret_type

    rt_args = list(sig.args)
    if target.decl.kind == FUNC_NORMAL:
        rt_args[0] = RuntimeArg(sig.args[0].name, RInstance(cls))

    arg_info = get_args(builder, rt_args, line)
    args, arg_kinds, arg_names = arg_info.args, arg_info.arg_kinds, arg_info.arg_names

    # We can do a passthrough *args/**kwargs with a native call, but if the
    # args need to get distributed out to arguments, we just let python handle it
    if (
        any(kind.is_star() for kind in arg_kinds)
        and any(not arg.kind.is_star() for arg in target.decl.sig.args)
    ):
        do_pycall = True

    if do_pycall:
        if target.decl.kind == FUNC_STATICMETHOD:
            # FIXME: this won't work if we can do interpreted subclasses
            first = builder.builder.get_native_type(cls)
            st = 0
        else:
            first = args[0]
            st = 1
        retval = builder.builder.py_method_call(
            first, target.name, args[st:], line, arg_kinds[st:], arg_names[st:])
    else:
        retval = builder.builder.call(target.decl, args, arg_kinds, arg_names, line)
    retval = builder.coerce(retval, sig.ret_type, line)
    builder.add(Return(retval))

    arg_regs, _, blocks, ret_type, _ = builder.leave()
    return FuncIR(
        FuncDecl(target.name + '__' + base.name + '_glue',
                 cls.name, builder.module_name,
                 FuncSignature(rt_args, ret_type),
                 target.decl.kind),
        arg_regs, blocks)


def gen_glue_property(builder: IRBuilder,
                      sig: FuncSignature,
                      target: FuncIR,
                      cls: ClassIR,
                      base: ClassIR,
                      line: int,
                      do_pygetattr: bool) -> FuncIR:
    """Generate glue methods for properties that mediate between different subclass types.

    Similarly to methods, properties of derived types can be covariantly subtyped. Thus,
    properties also require glue. However, this only requires the return type to change.
    Further, instead of a method call, an attribute get is performed.

    If do_pygetattr is True, then get the attribute using the Python C
    API instead of a native call.
    """
    builder.enter()

    rt_arg = RuntimeArg(SELF_NAME, RInstance(cls))
    self_target = builder.add_self_to_env(cls)
    arg = builder.read(self_target, line)
    builder.ret_types[-1] = sig.ret_type
    if do_pygetattr:
        retval = builder.py_get_attr(arg, target.name, line)
    else:
        retval = builder.add(GetAttr(arg, target.name, line))
    retbox = builder.coerce(retval, sig.ret_type, line)
    builder.add(Return(retbox))

    args, _, blocks, return_type, _ = builder.leave()
    return FuncIR(
        FuncDecl(target.name + '__' + base.name + '_glue',
                 cls.name, builder.module_name, FuncSignature([rt_arg], return_type)),
        args, blocks)


def get_func_target(builder: IRBuilder, fdef: FuncDef) -> AssignmentTarget:
    """Given a FuncDef, return the target for the instance of its callable class.

    If the function was not already defined somewhere, then define it
    and add it to the current environment.
    """
    if fdef.original_def:
        # Get the target associated with the previously defined FuncDef.
        return builder.lookup(fdef.original_def)

    if builder.fn_info.is_generator or builder.fn_info.contains_nested:
        return builder.lookup(fdef)

    return builder.add_local_reg(fdef, object_rprimitive)


def load_type(builder: IRBuilder, typ: TypeInfo, line: int) -> Value:
    if typ in builder.mapper.type_to_ir:
        class_ir = builder.mapper.type_to_ir[typ]
        class_obj = builder.builder.get_native_type(class_ir)
    elif typ.fullname in builtin_names:
        builtin_addr_type, src = builtin_names[typ.fullname]
        class_obj = builder.add(LoadAddress(builtin_addr_type, src, line))
    else:
        class_obj = builder.load_global_str(typ.name, line)

    return class_obj


def load_func(builder: IRBuilder, func_name: str, fullname: Optional[str], line: int) -> Value:
    if fullname is not None and not fullname.startswith(builder.current_module):
        # we're calling a function in a different module

        # We can't use load_module_attr_by_fullname here because we need to load the function using
        # func_name, not the name specified by fullname (which can be different for underscore
        # function)
        module = fullname.rsplit('.')[0]
        loaded_module = builder.load_module(module)

        func = builder.py_get_attr(loaded_module, func_name, line)
    else:
        func = builder.load_global_str(func_name, line)
    return func


def generate_singledispatch_dispatch_function(
    builder: IRBuilder,
    main_singledispatch_function_name: str,
    fitem: FuncDef,
) -> None:
    line = fitem.line
    current_func_decl = builder.mapper.func_to_decl[fitem]
    arg_info = get_args(builder, current_func_decl.sig.args, line)

    dispatch_func_obj = builder.self()

    arg_type = builder.builder.get_type_of_obj(arg_info.args[0], line)
    dispatch_cache = builder.builder.get_attr(
        dispatch_func_obj, 'dispatch_cache', dict_rprimitive, line
    )
    call_find_impl, use_cache, call_func = BasicBlock(), BasicBlock(), BasicBlock()
    get_result = builder.call_c(dict_get_method_with_none, [dispatch_cache, arg_type], line)
    is_not_none = builder.translate_is_op(get_result, builder.none_object(), 'is not', line)
    impl_to_use = Register(object_rprimitive)
    builder.add_bool_branch(is_not_none, use_cache, call_find_impl)

    builder.activate_block(use_cache)
    builder.assign(impl_to_use, get_result, line)
    builder.goto(call_func)

    builder.activate_block(call_find_impl)
    find_impl = builder.load_module_attr_by_fullname('functools._find_impl', line)
    registry = load_singledispatch_registry(builder, dispatch_func_obj, line)
    uncached_impl = builder.py_call(find_impl, [arg_type, registry], line)
    builder.call_c(dict_set_item_op, [dispatch_cache, arg_type, uncached_impl], line)
    builder.assign(impl_to_use, uncached_impl, line)
    builder.goto(call_func)

    builder.activate_block(call_func)
    gen_calls_to_correct_impl(builder, impl_to_use, arg_info, fitem, line)


def gen_calls_to_correct_impl(
    builder: IRBuilder,
    impl_to_use: Value,
    arg_info: ArgInfo,
    fitem: FuncDef,
    line: int,
) -> None:
    current_func_decl = builder.mapper.func_to_decl[fitem]

    def gen_native_func_call_and_return(fdef: FuncDef) -> None:
        func_decl = builder.mapper.func_to_decl[fdef]
        ret_val = builder.builder.call(
            func_decl, arg_info.args, arg_info.arg_kinds, arg_info.arg_names, line
        )
        coerced = builder.coerce(ret_val, current_func_decl.sig.ret_type, line)
        builder.add(Return(coerced))

    typ, src = builtin_names['builtins.int']
    int_type_obj = builder.add(LoadAddress(typ, src, line))
    is_int = builder.builder.type_is_op(impl_to_use, int_type_obj, line)

    native_call, non_native_call = BasicBlock(), BasicBlock()
    builder.add_bool_branch(is_int, native_call, non_native_call)
    builder.activate_block(native_call)

    passed_id = builder.add(Unbox(impl_to_use, int_rprimitive, line))

    native_ids = get_native_impl_ids(builder, fitem)
    for impl, i in native_ids.items():
        call_impl, next_impl = BasicBlock(), BasicBlock()

        current_id = builder.load_int(i)
        builder.builder.compare_tagged_condition(
            passed_id,
            current_id,
            '==',
            call_impl,
            next_impl,
            line,
        )

        # Call the registered implementation
        builder.activate_block(call_impl)

        gen_native_func_call_and_return(impl)
        builder.activate_block(next_impl)

    # We've already handled all the possible integer IDs, so we should never get here
    builder.add(Unreachable())

    builder.activate_block(non_native_call)
    ret_val = builder.py_call(
        impl_to_use, arg_info.args, line, arg_info.arg_kinds, arg_info.arg_names
    )
    coerced = builder.coerce(ret_val, current_func_decl.sig.ret_type, line)
    builder.add(Return(coerced))


def gen_dispatch_func_ir(
    builder: IRBuilder,
    fitem: FuncDef,
    main_func_name: str,
    dispatch_name: str,
    sig: FuncSignature,
) -> Tuple[FuncIR, Value]:
    """Create a dispatch function (a function that checks the first argument type and dispatches
    to the correct implementation)
    """
    builder.enter(FuncInfo(fitem, dispatch_name))
    setup_callable_class(builder)
    builder.fn_info.callable_class.ir.attributes['registry'] = dict_rprimitive
    builder.fn_info.callable_class.ir.attributes['dispatch_cache'] = dict_rprimitive
    builder.fn_info.callable_class.ir.has_dict = True
    builder.fn_info.callable_class.ir.needs_getseters = True
    generate_singledispatch_callable_class_ctor(builder)

    generate_singledispatch_dispatch_function(builder, main_func_name, fitem)
    args, _, blocks, _, fn_info = builder.leave()
    dispatch_callable_class = add_call_to_callable_class(builder, args, blocks, sig, fn_info)
    builder.functions.append(dispatch_callable_class)
    add_get_to_callable_class(builder, fn_info)
    add_register_method_to_callable_class(builder, fn_info)
    func_reg = instantiate_callable_class(builder, fn_info)
    dispatch_func_ir = generate_dispatch_glue_native_function(
        builder, fitem, dispatch_callable_class.decl, dispatch_name
    )

    return dispatch_func_ir, func_reg


def generate_dispatch_glue_native_function(
    builder: IRBuilder,
    fitem: FuncDef,
    callable_class_decl: FuncDecl,
    dispatch_name: str,
) -> FuncIR:
    line = fitem.line
    builder.enter()
    # We store the callable class in the globals dict for this function
    callable_class = builder.load_global_str(dispatch_name, line)
    decl = builder.mapper.func_to_decl[fitem]
    arg_info = get_args(builder, decl.sig.args, line)
    args = [callable_class] + arg_info.args
    arg_kinds = [ArgKind.ARG_POS] + arg_info.arg_kinds
    arg_names = arg_info.arg_names
    arg_names.insert(0, 'self')
    ret_val = builder.builder.call(callable_class_decl, args, arg_kinds, arg_names, line)
    builder.add(Return(ret_val))
    arg_regs, _, blocks, _, fn_info = builder.leave()
    return FuncIR(decl, arg_regs, blocks)


def generate_singledispatch_callable_class_ctor(builder: IRBuilder) -> None:
    """Create an __init__ that sets registry and dispatch_cache to empty dicts"""
    line = -1
    class_ir = builder.fn_info.callable_class.ir
    with builder.enter_method(class_ir, '__init__', bool_rprimitive):
        empty_dict = builder.call_c(dict_new_op, [], line)
        builder.add(SetAttr(builder.self(), 'registry', empty_dict, line))
        cache_dict = builder.call_c(dict_new_op, [], line)
        dispatch_cache_str = builder.load_str('dispatch_cache')
        # use the py_setattr_op instead of SetAttr so that it also gets added to our __dict__
        builder.call_c(py_setattr_op, [builder.self(), dispatch_cache_str, cache_dict], line)
        # the generated C code seems to expect that __init__ returns a char, so just return 1
        builder.add(Return(Integer(1, bool_rprimitive, line), line))


def add_register_method_to_callable_class(builder: IRBuilder, fn_info: FuncInfo) -> None:
    line = -1
    with builder.enter_method(fn_info.callable_class.ir, 'register', object_rprimitive):
        cls_arg = builder.add_argument('cls', object_rprimitive)
        func_arg = builder.add_argument('func', object_rprimitive, ArgKind.ARG_OPT)
        ret_val = builder.call_c(register_function, [builder.self(), cls_arg, func_arg], line)
        builder.add(Return(ret_val, line))


def load_singledispatch_registry(builder: IRBuilder, dispatch_func_obj: Value, line: int) -> Value:
    return builder.builder.get_attr(dispatch_func_obj, 'registry', dict_rprimitive, line)


def singledispatch_main_func_name(orig_name: str) -> str:
    return f'__mypyc_singledispatch_main_function_{orig_name}__'


def get_registry_identifier(fitem: FuncDef) -> str:
    return f'__mypyc_singledispatch_registry_{fitem.fullname}__'


def maybe_insert_into_registry_dict(builder: IRBuilder, fitem: FuncDef) -> None:
    line = fitem.line
    is_singledispatch_main_func = fitem in builder.singledispatch_impls
    # dict of singledispatch_func to list of register_types (fitem is the function to register)
    to_register: DefaultDict[FuncDef, List[TypeInfo]] = defaultdict(list)
    for main_func, impls in builder.singledispatch_impls.items():
        for dispatch_type, impl in impls:
            if fitem == impl:
                to_register[main_func].append(dispatch_type)

    if not to_register and not is_singledispatch_main_func:
        return

    if is_singledispatch_main_func:
        main_func_name = singledispatch_main_func_name(fitem.name)
        main_func_obj = load_func(builder, main_func_name, fitem.fullname, line)

        loaded_object_type = builder.load_module_attr_by_fullname('builtins.object', line)
        registry_dict = builder.builder.make_dict([(loaded_object_type, main_func_obj)], line)

        dispatch_func_obj = builder.load_global_str(fitem.name, line)
        builder.call_c(
            py_setattr_op, [dispatch_func_obj, builder.load_str('registry'), registry_dict], line
        )

    for singledispatch_func, types in to_register.items():
        # TODO: avoid recomputing the native IDs for all the functions every time we find a new
        # function
        native_ids = get_native_impl_ids(builder, singledispatch_func)
        if fitem not in native_ids:
            to_insert = load_func(builder, fitem.name, fitem.fullname, line)
        else:
            current_id = native_ids[fitem]
            load_literal = LoadLiteral(current_id, object_rprimitive)
            to_insert = builder.add(load_literal)
        # TODO: avoid reloading the registry here if we just created it
        dispatch_func_obj = load_func(
            builder, singledispatch_func.name, singledispatch_func.fullname, line
        )
        registry = load_singledispatch_registry(builder, dispatch_func_obj, line)
        for typ in types:
            loaded_type = load_type(builder, typ, line)
            builder.call_c(dict_set_item_op, [registry, loaded_type, to_insert], line)
        dispatch_cache = builder.builder.get_attr(
            dispatch_func_obj, 'dispatch_cache', dict_rprimitive, line
        )
        builder.gen_method_call(dispatch_cache, 'clear', [], None, line)


def get_native_impl_ids(builder: IRBuilder, singledispatch_func: FuncDef) -> Dict[FuncDef, int]:
    """Return a dict of registered implementation to native implementation ID for all
    implementations
    """
    impls = builder.singledispatch_impls[singledispatch_func]
    return {impl: i for i, (typ, impl) in enumerate(impls) if not is_decorated(builder, impl)}
