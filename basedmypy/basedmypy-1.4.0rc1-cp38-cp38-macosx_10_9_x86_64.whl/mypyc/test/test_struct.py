import unittest

from mypyc.ir.rtypes import (
    RStruct, bool_rprimitive, int64_rprimitive, int32_rprimitive, object_rprimitive,
    int_rprimitive
)
from mypyc.rt_subtype import is_runtime_subtype


class TestStruct(unittest.TestCase):
    def test_struct_offsets(self) -> None:
        # test per-member alignment
        r = RStruct("", [], [bool_rprimitive, int32_rprimitive, int64_rprimitive])
        assert r.size == 16
        assert r.offsets == [0, 4, 8]

        # test final alignment
        r1 = RStruct("", [], [bool_rprimitive, bool_rprimitive])
        assert r1.size == 2
        assert r1.offsets == [0, 1]
        r2 = RStruct("", [], [int32_rprimitive, bool_rprimitive])
        r3 = RStruct("", [], [int64_rprimitive, bool_rprimitive])
        assert r2.offsets == [0, 4]
        assert r3.offsets == [0, 8]
        assert r2.size == 8
        assert r3.size == 16

        r4 = RStruct("", [], [bool_rprimitive, bool_rprimitive,
                              bool_rprimitive, int32_rprimitive])
        assert r4.size == 8
        assert r4.offsets == [0, 1, 2, 4]

        # test nested struct
        r5 = RStruct("", [], [bool_rprimitive, r])
        assert r5.offsets == [0, 8]
        assert r5.size == 24
        r6 = RStruct("", [], [int32_rprimitive, r5])
        assert r6.offsets == [0, 8]
        assert r6.size == 32
        # test nested struct with alignment less than 8
        r7 = RStruct("", [], [bool_rprimitive, r4])
        assert r7.offsets == [0, 4]
        assert r7.size == 12

    def test_struct_str(self) -> None:
        r = RStruct("Foo", ["a", "b"],
                    [bool_rprimitive, object_rprimitive])
        assert str(r) == "Foo{a:bool, b:object}"
        assert repr(r) == "<RStruct Foo{a:<RPrimitive builtins.bool>, " \
                          "b:<RPrimitive builtins.object>}>"
        r1 = RStruct("Bar", ["c"], [int32_rprimitive])
        assert str(r1) == "Bar{c:int32}"
        assert repr(r1) == "<RStruct Bar{c:<RPrimitive int32>}>"
        r2 = RStruct("Baz", [], [])
        assert str(r2) == "Baz{}"
        assert repr(r2) == "<RStruct Baz{}>"

    def test_runtime_subtype(self) -> None:
        # right type to check with
        r = RStruct("Foo", ["a", "b"],
                    [bool_rprimitive, int_rprimitive])

        # using the exact same fields
        r1 = RStruct("Foo", ["a", "b"],
                    [bool_rprimitive, int_rprimitive])

        # names different
        r2 = RStruct("Bar", ["c", "b"],
                    [bool_rprimitive, int_rprimitive])

        # name different
        r3 = RStruct("Baz", ["a", "b"],
                    [bool_rprimitive, int_rprimitive])

        # type different
        r4 = RStruct("FooBar", ["a", "b"],
                    [bool_rprimitive, int32_rprimitive])

        # number of types different
        r5 = RStruct("FooBarBaz", ["a", "b", "c"],
                    [bool_rprimitive, int_rprimitive, bool_rprimitive])

        assert is_runtime_subtype(r1, r) is True
        assert is_runtime_subtype(r2, r) is False
        assert is_runtime_subtype(r3, r) is False
        assert is_runtime_subtype(r4, r) is False
        assert is_runtime_subtype(r5, r) is False

    def test_eq_and_hash(self) -> None:
        r = RStruct("Foo", ["a", "b"],
                    [bool_rprimitive, int_rprimitive])

        # using the exact same fields
        r1 = RStruct("Foo", ["a", "b"],
                    [bool_rprimitive, int_rprimitive])
        assert hash(r) == hash(r1)
        assert r == r1

        # different name
        r2 = RStruct("Foq", ["a", "b"],
                    [bool_rprimitive, int_rprimitive])
        assert hash(r) != hash(r2)
        assert r != r2

        # different names
        r3 = RStruct("Foo", ["a", "c"],
                    [bool_rprimitive, int_rprimitive])
        assert hash(r) != hash(r3)
        assert r != r3

        # different type
        r4 = RStruct("Foo", ["a", "b"],
                    [bool_rprimitive, int_rprimitive, bool_rprimitive])
        assert hash(r) != hash(r4)
        assert r != r4
