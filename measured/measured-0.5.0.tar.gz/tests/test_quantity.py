from typing import Any

import pytest

from measured import Length, Numeric, One, Quantity, Unit
from measured.si import Meter, Ohm, Second


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    examples = [
        5 * Meter,
        10 * Meter / Second,
        10.5 * Ohm,
    ]

    ids = [str(q) for q in examples]

    if "quantity" in metafunc.fixturenames:
        metafunc.parametrize("quantity", examples, ids=ids)


@pytest.mark.parametrize("value", [-2, 5, 0.1, -0.3, 2.5])
def test_constructing_quantities_by_multiplying_units(value: Numeric) -> None:
    assert Meter * value == value * Meter
    assert value * Meter * Meter == value * Meter**2
    assert value * Meter / Second == value * (Meter / Second)


@pytest.mark.parametrize("value", ["nope", b"nah"])
def test_construction_by_multiplication_only_with_number_types(value: Any) -> None:
    with pytest.raises(TypeError):
        Meter * value

    with pytest.raises(TypeError):
        value * Meter


@pytest.mark.parametrize("value", ["nope", b"nah"])
def test_construction_by_division_only_with_number_types(value: Any) -> None:
    with pytest.raises(TypeError):
        Meter / value

    with pytest.raises(TypeError):
        value / Meter


def test_equality_only_with_quantities() -> None:
    assert 5 * One != 5
    assert 5 * Meter != 5
    assert 5 * Meter != Meter


def test_equality_only_in_same_dimension() -> None:
    assert 5 * Meter != 5 * Second


def test_addition_only_with_quantities() -> None:
    with pytest.raises(TypeError):
        (5 * Meter) + 10  # type: ignore

    with pytest.raises(TypeError):
        10 + (5 * Meter)  # type: ignore


def test_subtraction_only_with_quantities() -> None:
    with pytest.raises(TypeError):
        (5 * Meter) - 10  # type: ignore

    with pytest.raises(TypeError):
        10 - (5 * Meter)  # type: ignore


def test_multiplication_by_scalar() -> None:
    assert 10 * (5 * Meter) == 50 * Meter


def test_division_by_scalar() -> None:
    assert (500 * Meter) / 10 == 50 * Meter


def test_exponentation_by_scalar() -> None:
    assert (5 * Meter) ** 2 == 25 * Meter**2


def test_roots() -> None:
    assert (10 * Meter).root(0) == 1 * One
    assert ((10 * Meter) ** 2).root(2) == 10 * Meter
    assert (100 * Meter**2).root(2) == 10 * Meter
    (64 * Meter**3).root(3).assert_approximates(4 * Meter)


def test_cannot_multiply_by_random_types() -> None:
    with pytest.raises(TypeError):
        "hi" * (5 * Meter)  # type: ignore

    with pytest.raises(TypeError):
        (5 * Meter) * "hi"  # type: ignore


def test_cannot_divide_by_random_types() -> None:
    with pytest.raises(TypeError):
        (5 * Meter) / "hi"  # type: ignore


def test_repr(quantity: Quantity) -> None:
    assert (
        repr(quantity)
        == f"Quantity(magnitude={quantity.magnitude!r}, unit={quantity.unit!r})"
    )


def test_repr_roundtrips(quantity: Quantity) -> None:
    from measured import Dimension, Prefix, Unit  # noqa: F401

    assert eval(repr(quantity)) == quantity


def test_negative() -> None:
    assert -(5 * Meter) == -5 * Meter


def test_positive() -> None:
    assert +(5 * Meter) == +5 * Meter


def test_absolute_value() -> None:
    assert abs(-5 * Meter) == 5 * Meter


def test_ordering() -> None:
    assert (-5 * Meter) < (1 * Meter)
    assert (1 * Meter) > (-5 * Meter)
    assert (1 * Meter) >= (1 * Meter)
    assert (1 * Meter) <= (1 * Meter)


def test_ordering_only_with_quantities() -> None:
    with pytest.raises(TypeError):
        1 * Meter <= 1


def test_ordering_only_within_dimension() -> None:
    with pytest.raises(TypeError):
        1 * Meter < 1 * Second

    with pytest.raises(TypeError):
        1 * Meter <= 1 * Second

    with pytest.raises(TypeError):
        1 * Meter > 1 * Second

    with pytest.raises(TypeError):
        1 * Meter >= 1 * Second


def test_ordering_requires_types_with_a_conversion() -> None:
    Bogie = Unit.define(Length, name="bogie", symbol="bogie")

    one = 1 * Meter
    other = 1 * Bogie

    with pytest.raises(TypeError):
        one < other

    with pytest.raises(TypeError):
        one <= other

    with pytest.raises(TypeError):
        one > other

    with pytest.raises(TypeError):
        one >= other


def test_ordering_requires_types_in_the_same_dimension() -> None:
    one = 1 * Meter
    other = 1 * Second

    with pytest.raises(TypeError):
        one < other

    with pytest.raises(TypeError):
        one <= other

    with pytest.raises(TypeError):
        one > other

    with pytest.raises(TypeError):
        one >= other


def test_sorting() -> None:
    unsorted = [1 * Meter, 0 * Meter, 5 * Meter]
    assert sorted(unsorted) == [0 * Meter, 1 * Meter, 5 * Meter]


def test_approximating() -> None:
    (1 * Meter).assert_approximates(1.0 * Meter)
    (1 * Meter).assert_approximates(1 * Meter)
    (1.0 * Meter).assert_approximates(1.0 * Meter)
    (1 * Meter).assert_approximates(1.0000000001 * Meter)
    assert not (1 * Meter).approximates(1.01 * Meter)
    assert not (1 * Meter).approximates(1.0 * Second)
