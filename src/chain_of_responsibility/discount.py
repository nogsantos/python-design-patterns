# -*- coding: utf-8 -*-
from typing import TypeVar

from src.chain_of_responsibility.budget import Budget

# https://docs.python.org/3/library/typing.html#user-defined-generic-types
T = TypeVar('T')


#
# Calculates the discount when the list has more than 5 items
#
class ByFiveItems:

    def __init__(self, next_discount: T) -> None:
        self.__next_discount = next_discount

    def calculate(self, budget: Budget) -> float:
        result = budget.total * 0.1 if budget.items_len > 5 else self.__next_discount.calculate(budget)
        return round(result, 3)


#
# Calculates the discount when total of items is grater than 500
#
class GraterThanFiveHundred:

    def __init__(self, next_discount: T) -> None:
        self.__next_discount = next_discount

    def calculate(self, budget: Budget) -> float:
        result = budget.total * 0.07 if budget.total > 500 else self.__next_discount.calculate(budget)
        return round(result, 3)


#
# When the budget has no discount
#
class WithoutDiscount:

    def calculate(self, budget: Budget) -> float:
        return 0.0
