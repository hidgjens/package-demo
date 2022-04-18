from __future__ import annotations

from typing import Type, overload


@overload
def add(lhs: int, rhs: int) -> int:
    ...


@overload
def add(lhs: float, rhs: int) -> float:
    ...


@overload
def add(lhs: int, rhs: float) -> float:
    ...


@overload
def add(lhs: float, rhs: float) -> float:
    ...


def add(lhs: float | int, rhs: float | int) -> float | int:
    """
    Add two numbers together.

    :param lhs:
        Left-hand-side value
    :type lhs:
        float | int
    :param rhs:
        Right-hand-side value
    :type rhs:
        float | int
    :return:
        Result of the operation
    :rtype:
        float | int
    """
    if isinstance(lhs, int) and isinstance(rhs, int):
        ret_type: Type[float] | Type[int] = int
    else:
        ret_type = float
    return ret_type(lhs + rhs)


def divide(lhs: float | int, rhs: float | int) -> float:
    """
    Divide `lhs` by `rhs`.

    :param lhs:
        Left-hand-side value
    :type lhs:
        float | int
    :param rhs:
        Right-hand-side value
    :type rhs:
        float | int
    :return:
        Result of the operation
    :rtype:
        float
    """
    return float(lhs / rhs)
