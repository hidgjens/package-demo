from pprint import pprint

import hidgjens.calc as calc
import pytest


@pytest.mark.parametrize(
    "lhs,rhs,expected,type_",
    [
        (1, 2, 3, int),
        (3.0, 4.0, 7.0, float),
        (5, 6.0, 11.0, float),
        (7.0, 8, 15.0, float),
        (1, -2, -1, int),
        (7.0, -8, -1.0, float),
    ],
)
def test_add(lhs, rhs, expected, type_):
    value = calc.add(lhs, rhs)
    assert value == expected
    assert isinstance(value, type_)


@pytest.mark.parametrize(
    "lhs,rhs,expected,",
    [
        (1, 2, 0.5),
        (4, 2, 2.0),
        (10, -5, -2.0),
        (2.0, 1.0, 2.0),
        (2.0, -1.0, -2.0),
    ],
)
def test_divide(lhs, rhs, expected):
    value = calc.divide(lhs, rhs)
    assert value == expected


def test_divide_by_zero_err():
    with pytest.raises(ZeroDivisionError):
        _ = calc.divide(1, 0)


def test_fixture(config_dict):
    pprint(config_dict)
