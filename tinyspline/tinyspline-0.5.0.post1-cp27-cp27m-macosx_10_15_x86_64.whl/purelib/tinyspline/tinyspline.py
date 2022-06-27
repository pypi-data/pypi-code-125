# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _tinysplinepython
else:
    import _tinysplinepython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _tinysplinepython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _tinysplinepython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


TS_PI = _tinysplinepython.TS_PI
TS_MAX_NUM_KNOTS = _tinysplinepython.TS_MAX_NUM_KNOTS
TS_DOMAIN_DEFAULT_MIN = _tinysplinepython.TS_DOMAIN_DEFAULT_MIN
TS_DOMAIN_DEFAULT_MAX = _tinysplinepython.TS_DOMAIN_DEFAULT_MAX
TS_KNOT_EPSILON = _tinysplinepython.TS_KNOT_EPSILON
TS_POINT_EPSILON = _tinysplinepython.TS_POINT_EPSILON
TS_LENGTH_ZERO = _tinysplinepython.TS_LENGTH_ZERO
class Vec2(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args):
        _tinysplinepython.Vec2_swiginit(self, _tinysplinepython.new_Vec2(*args))
    __add__ = _swig_new_instance_method(_tinysplinepython.Vec2___add__)
    __sub__ = _swig_new_instance_method(_tinysplinepython.Vec2___sub__)
    __mul__ = _swig_new_instance_method(_tinysplinepython.Vec2___mul__)
    add = _swig_new_instance_method(_tinysplinepython.Vec2_add)
    subtract = _swig_new_instance_method(_tinysplinepython.Vec2_subtract)
    multiply = _swig_new_instance_method(_tinysplinepython.Vec2_multiply)
    normalize = _swig_new_instance_method(_tinysplinepython.Vec2_normalize)
    norm = _swig_new_instance_method(_tinysplinepython.Vec2_norm)
    magnitude = _swig_new_instance_method(_tinysplinepython.Vec2_magnitude)
    dot = _swig_new_instance_method(_tinysplinepython.Vec2_dot)
    angle = _swig_new_instance_method(_tinysplinepython.Vec2_angle)
    distance = _swig_new_instance_method(_tinysplinepython.Vec2_distance)
    __repr__ = _swig_new_instance_method(_tinysplinepython.Vec2___repr__)
    x = property(_tinysplinepython.Vec2_x_get, _tinysplinepython.Vec2_x_set)
    y = property(_tinysplinepython.Vec2_y_get, _tinysplinepython.Vec2_y_set)
    values = property(_tinysplinepython.Vec2_values_get)
    __swig_destroy__ = _tinysplinepython.delete_Vec2

# Register Vec2 in _tinysplinepython:
_tinysplinepython.Vec2_swigregister(Vec2)

class Vec3(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args):
        _tinysplinepython.Vec3_swiginit(self, _tinysplinepython.new_Vec3(*args))
    __add__ = _swig_new_instance_method(_tinysplinepython.Vec3___add__)
    __sub__ = _swig_new_instance_method(_tinysplinepython.Vec3___sub__)
    __mul__ = _swig_new_instance_method(_tinysplinepython.Vec3___mul__)
    add = _swig_new_instance_method(_tinysplinepython.Vec3_add)
    subtract = _swig_new_instance_method(_tinysplinepython.Vec3_subtract)
    multiply = _swig_new_instance_method(_tinysplinepython.Vec3_multiply)
    cross = _swig_new_instance_method(_tinysplinepython.Vec3_cross)
    normalize = _swig_new_instance_method(_tinysplinepython.Vec3_normalize)
    norm = _swig_new_instance_method(_tinysplinepython.Vec3_norm)
    magnitude = _swig_new_instance_method(_tinysplinepython.Vec3_magnitude)
    dot = _swig_new_instance_method(_tinysplinepython.Vec3_dot)
    angle = _swig_new_instance_method(_tinysplinepython.Vec3_angle)
    distance = _swig_new_instance_method(_tinysplinepython.Vec3_distance)
    __repr__ = _swig_new_instance_method(_tinysplinepython.Vec3___repr__)
    x = property(_tinysplinepython.Vec3_x_get, _tinysplinepython.Vec3_x_set)
    y = property(_tinysplinepython.Vec3_y_get, _tinysplinepython.Vec3_y_set)
    z = property(_tinysplinepython.Vec3_z_get, _tinysplinepython.Vec3_z_set)
    values = property(_tinysplinepython.Vec3_values_get)
    __swig_destroy__ = _tinysplinepython.delete_Vec3

# Register Vec3 in _tinysplinepython:
_tinysplinepython.Vec3_swigregister(Vec3)

class Vec4(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args):
        _tinysplinepython.Vec4_swiginit(self, _tinysplinepython.new_Vec4(*args))
    __add__ = _swig_new_instance_method(_tinysplinepython.Vec4___add__)
    __sub__ = _swig_new_instance_method(_tinysplinepython.Vec4___sub__)
    __mul__ = _swig_new_instance_method(_tinysplinepython.Vec4___mul__)
    add = _swig_new_instance_method(_tinysplinepython.Vec4_add)
    subtract = _swig_new_instance_method(_tinysplinepython.Vec4_subtract)
    multiply = _swig_new_instance_method(_tinysplinepython.Vec4_multiply)
    normalize = _swig_new_instance_method(_tinysplinepython.Vec4_normalize)
    norm = _swig_new_instance_method(_tinysplinepython.Vec4_norm)
    magnitude = _swig_new_instance_method(_tinysplinepython.Vec4_magnitude)
    dot = _swig_new_instance_method(_tinysplinepython.Vec4_dot)
    angle = _swig_new_instance_method(_tinysplinepython.Vec4_angle)
    distance = _swig_new_instance_method(_tinysplinepython.Vec4_distance)
    __repr__ = _swig_new_instance_method(_tinysplinepython.Vec4___repr__)
    x = property(_tinysplinepython.Vec4_x_get, _tinysplinepython.Vec4_x_set)
    y = property(_tinysplinepython.Vec4_y_get, _tinysplinepython.Vec4_y_set)
    z = property(_tinysplinepython.Vec4_z_get, _tinysplinepython.Vec4_z_set)
    w = property(_tinysplinepython.Vec4_w_get, _tinysplinepython.Vec4_w_set)
    values = property(_tinysplinepython.Vec4_values_get)
    __swig_destroy__ = _tinysplinepython.delete_Vec4

# Register Vec4 in _tinysplinepython:
_tinysplinepython.Vec4_swigregister(Vec4)

class Frame(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, position, tangent, normal, binormal):
        _tinysplinepython.Frame_swiginit(self, _tinysplinepython.new_Frame(position, tangent, normal, binormal))
    __repr__ = _swig_new_instance_method(_tinysplinepython.Frame___repr__)
    position = property(_tinysplinepython.Frame_position_get)
    tangent = property(_tinysplinepython.Frame_tangent_get)
    normal = property(_tinysplinepython.Frame_normal_get)
    binormal = property(_tinysplinepython.Frame_binormal_get)
    __swig_destroy__ = _tinysplinepython.delete_Frame

# Register Frame in _tinysplinepython:
_tinysplinepython.Frame_swigregister(Frame)

class FrameSeq(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args):
        _tinysplinepython.FrameSeq_swiginit(self, _tinysplinepython.new_FrameSeq(*args))
    __swig_destroy__ = _tinysplinepython.delete_FrameSeq
    size = _swig_new_instance_method(_tinysplinepython.FrameSeq_size)
    at = _swig_new_instance_method(_tinysplinepython.FrameSeq_at)
    __repr__ = _swig_new_instance_method(_tinysplinepython.FrameSeq___repr__)

# Register FrameSeq in _tinysplinepython:
_tinysplinepython.FrameSeq_swigregister(FrameSeq)

class Domain(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, min, max):
        _tinysplinepython.Domain_swiginit(self, _tinysplinepython.new_Domain(min, max))
    __repr__ = _swig_new_instance_method(_tinysplinepython.Domain___repr__)
    min = property(_tinysplinepython.Domain_min_get)
    max = property(_tinysplinepython.Domain_max_get)
    __swig_destroy__ = _tinysplinepython.delete_Domain

# Register Domain in _tinysplinepython:
_tinysplinepython.Domain_swigregister(Domain)

class DeBoorNet(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, other):
        _tinysplinepython.DeBoorNet_swiginit(self, _tinysplinepython.new_DeBoorNet(other))
    __swig_destroy__ = _tinysplinepython.delete_DeBoorNet
    result_vec2 = _swig_new_instance_method(_tinysplinepython.DeBoorNet_result_vec2)
    result_vec3 = _swig_new_instance_method(_tinysplinepython.DeBoorNet_result_vec3)
    result_vec4 = _swig_new_instance_method(_tinysplinepython.DeBoorNet_result_vec4)
    __repr__ = _swig_new_instance_method(_tinysplinepython.DeBoorNet___repr__)
    knot = property(_tinysplinepython.DeBoorNet_knot_get)
    index = property(_tinysplinepython.DeBoorNet_index_get)
    multiplicity = property(_tinysplinepython.DeBoorNet_multiplicity_get)
    num_insertions = property(_tinysplinepython.DeBoorNet_num_insertions_get)
    dimension = property(_tinysplinepython.DeBoorNet_dimension_get)
    points = property(_tinysplinepython.DeBoorNet_points_get)
    result = property(_tinysplinepython.DeBoorNet_result_get)

# Register DeBoorNet in _tinysplinepython:
_tinysplinepython.DeBoorNet_swigregister(DeBoorNet)

class BSpline(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    Opened = _tinysplinepython.BSpline_Opened
    Clamped = _tinysplinepython.BSpline_Clamped
    Beziers = _tinysplinepython.BSpline_Beziers

    def __init__(self, *args):
        _tinysplinepython.BSpline_swiginit(self, _tinysplinepython.new_BSpline(*args))
    __swig_destroy__ = _tinysplinepython.delete_BSpline
    interpolate_cubic_natural = _swig_new_static_method(_tinysplinepython.BSpline_interpolate_cubic_natural)
    interpolate_catmull_rom = _swig_new_static_method(_tinysplinepython.BSpline_interpolate_catmull_rom)
    parse_json = _swig_new_static_method(_tinysplinepython.BSpline_parse_json)
    load = _swig_new_static_method(_tinysplinepython.BSpline_load)
    knots_equal = _swig_new_static_method(_tinysplinepython.BSpline_knots_equal)
    __call__ = _swig_new_instance_method(_tinysplinepython.BSpline___call__)
    control_point_vec2_at = _swig_new_instance_method(_tinysplinepython.BSpline_control_point_vec2_at)
    control_point_vec3_at = _swig_new_instance_method(_tinysplinepython.BSpline_control_point_vec3_at)
    control_point_vec4_at = _swig_new_instance_method(_tinysplinepython.BSpline_control_point_vec4_at)
    knot_at = _swig_new_instance_method(_tinysplinepython.BSpline_knot_at)
    eval = _swig_new_instance_method(_tinysplinepython.BSpline_eval)
    eval_all = _swig_new_instance_method(_tinysplinepython.BSpline_eval_all)
    sample = _swig_new_instance_method(_tinysplinepython.BSpline_sample)
    bisect = _swig_new_instance_method(_tinysplinepython.BSpline_bisect)
    is_closed = _swig_new_instance_method(_tinysplinepython.BSpline_is_closed)
    compute_rmf = _swig_new_instance_method(_tinysplinepython.BSpline_compute_rmf)
    uniform_knot_seq = _swig_new_instance_method(_tinysplinepython.BSpline_uniform_knot_seq)
    to_json = _swig_new_instance_method(_tinysplinepython.BSpline_to_json)
    save = _swig_new_instance_method(_tinysplinepython.BSpline_save)
    set_control_point_vec2_at = _swig_new_instance_method(_tinysplinepython.BSpline_set_control_point_vec2_at)
    set_control_point_vec3_at = _swig_new_instance_method(_tinysplinepython.BSpline_set_control_point_vec3_at)
    set_control_point_vec4_at = _swig_new_instance_method(_tinysplinepython.BSpline_set_control_point_vec4_at)
    set_knot_at = _swig_new_instance_method(_tinysplinepython.BSpline_set_knot_at)
    insert_knot = _swig_new_instance_method(_tinysplinepython.BSpline_insert_knot)
    split = _swig_new_instance_method(_tinysplinepython.BSpline_split)
    tension = _swig_new_instance_method(_tinysplinepython.BSpline_tension)
    to_beziers = _swig_new_instance_method(_tinysplinepython.BSpline_to_beziers)
    derive = _swig_new_instance_method(_tinysplinepython.BSpline_derive)
    elevate_degree = _swig_new_instance_method(_tinysplinepython.BSpline_elevate_degree)
    align_with = _swig_new_instance_method(_tinysplinepython.BSpline_align_with)
    morph_to = _swig_new_instance_method(_tinysplinepython.BSpline_morph_to)
    __repr__ = _swig_new_instance_method(_tinysplinepython.BSpline___repr__)
    control_point_vec_2at = _swig_new_instance_method(_tinysplinepython.BSpline_control_point_vec_2at)
    set_control_point_vec_2at = _swig_new_instance_method(_tinysplinepython.BSpline_set_control_point_vec_2at)
    control_point_vec_3at = _swig_new_instance_method(_tinysplinepython.BSpline_control_point_vec_3at)
    set_control_point_vec_3at = _swig_new_instance_method(_tinysplinepython.BSpline_set_control_point_vec_3at)
    control_point_vec_4at = _swig_new_instance_method(_tinysplinepython.BSpline_control_point_vec_4at)
    set_control_point_vec_4at = _swig_new_instance_method(_tinysplinepython.BSpline_set_control_point_vec_4at)
    degree = property(_tinysplinepython.BSpline_degree_get)
    order = property(_tinysplinepython.BSpline_order_get)
    dimension = property(_tinysplinepython.BSpline_dimension_get)
    num_control_points = property(_tinysplinepython.BSpline_num_control_points_get)
    domain = property(_tinysplinepython.BSpline_domain_get)
    control_points = property(_tinysplinepython.BSpline_control_points_get, _tinysplinepython.BSpline_control_points_set)
    knots = property(_tinysplinepython.BSpline_knots_get, _tinysplinepython.BSpline_knots_set)

# Register BSpline in _tinysplinepython:
_tinysplinepython.BSpline_swigregister(BSpline)
BSpline_interpolate_cubic_natural = _tinysplinepython.BSpline_interpolate_cubic_natural
BSpline_interpolate_catmull_rom = _tinysplinepython.BSpline_interpolate_catmull_rom
BSpline_parse_json = _tinysplinepython.BSpline_parse_json
BSpline_load = _tinysplinepython.BSpline_load
BSpline_knots_equal = _tinysplinepython.BSpline_knots_equal

class Morphism(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, origin, target, epsilon=1e-5):
        _tinysplinepython.Morphism_swiginit(self, _tinysplinepython.new_Morphism(origin, target, epsilon))
    eval = _swig_new_instance_method(_tinysplinepython.Morphism_eval)
    __call__ = _swig_new_instance_method(_tinysplinepython.Morphism___call__)
    __repr__ = _swig_new_instance_method(_tinysplinepython.Morphism___repr__)
    origin = property(_tinysplinepython.Morphism_origin_get)
    target = property(_tinysplinepython.Morphism_target_get)
    epsilon = property(_tinysplinepython.Morphism_epsilon_get)
    __swig_destroy__ = _tinysplinepython.delete_Morphism

# Register Morphism in _tinysplinepython:
_tinysplinepython.Morphism_swigregister(Morphism)

class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _tinysplinepython.delete_SwigPyIterator
    value = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_value)
    incr = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_copy)
    next = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_tinysplinepython.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_tinysplinepython.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_tinysplinepython.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_tinysplinepython.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_tinysplinepython.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_tinysplinepython.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_tinysplinepython.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _tinysplinepython:
_tinysplinepython.SwigPyIterator_swigregister(SwigPyIterator)



