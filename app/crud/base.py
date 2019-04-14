from typing import TypeVar, Sequence
from sqlalchemy import and_, or_

T = TypeVar('T')


def and_equal(filters: list, model: Sequence[T], cond):
    return filters.append(and_(model == cond))


def or_equal(filters: list, model: Sequence[T], cond):
    return filters.append(or_(model == cond))


def and_greater_than(filters: list, model: Sequence[T], cond):
    return filters.append(and_(model >= cond))


def or_grater_than(filters: list, model: Sequence[T], cond):
    return filters.append(or_(model <= cond))


def and_less_than(filters: list, model: Sequence[T], cond):
    return filters.append(and_(model < cond))


def or_less_than(filters: list, model: Sequence[T], cond):
    return filters.append(or_(model < cond))
