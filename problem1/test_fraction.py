import pytest
from fraction import Fraction


def test_fraction_constructor():
    f = Fraction(7, 11)
    assert f.numerator == 7
    assert f.denominator == 11


def test_fraction_constructor_reduction():
    f = Fraction(100, 10)
    assert f.numerator == 10
    assert f.denominator == 1

    f = Fraction(28, 20)
    assert f.numerator == 7
    assert f.denominator == 5


def test_fraction_eq():
    assert Fraction(5, 3) == Fraction(5, 3)


def test_fraction_repr():
    assert repr(Fraction(5, 3)) == "Fraction(5, 3)"


def test_fraction_neg():
    assert -Fraction(5, 3) == Fraction(-5, 3)
    assert -Fraction(-5, 3) == Fraction(5, 3)


@pytest.mark.parametrize(
    "a,b,result",
    [
        (Fraction(3, 2), 1, Fraction(5, 2)),
        (1, Fraction(3, 2), Fraction(5, 2)),
        (Fraction(3, 2), Fraction(9, 10), Fraction(12, 5)),
    ],
)
def test_fraction_addition(a, b, result):
    assert a + b == result, f"Expected {result}, got {a+b}"


@pytest.mark.parametrize(
    "a,b,result",
    [
        (Fraction(3, 2), 1, Fraction(1, 2)),
        (1, Fraction(3, 2), Fraction(-1, 2)),
        (Fraction(3, 2), Fraction(9, 10), Fraction(3, 5)),
    ],
)
def test_fraction_subtraction(a, b, result):
    assert a - b == result, f"Expected {result}, got {a-b}"


@pytest.mark.parametrize(
    "a,b,result",
    [
        (Fraction(3, 2), 7, Fraction(21, 2)),
        (7, Fraction(3, 2), Fraction(21, 2)),
        (Fraction(3, 2), Fraction(9, 10), Fraction(27, 20)),
    ],
)
def test_fraction_multiplication(a, b, result):
    assert a * b == result, f"Expected {result}, got {a*b}"


@pytest.mark.parametrize(
    "a,b,result",
    [
        (Fraction(3, 2), 2, Fraction(3, 4)),
        (3, Fraction(3, 2), Fraction(2, 1)),
        (Fraction(3, 2), Fraction(9, 10), Fraction(5, 3)),
    ],
)
def test_fraction_division(a, b, result):
    assert a / b == result, f"Expected {result}, got {a/b}"
