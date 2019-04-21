# -*- coding: utf-8 -*-

from src.chain_of_responsibility.discount import Budget, ByFiveItems, GraterThanFiveHundred, WithoutDiscount


#
# The Chain of responsibility standard falls as a specific list, and is also the following in the scenario that
# must be validated, otherwise it is not a condition.
# In such cases, the Chain of Responsibility enables us to separate responsibilities from
# small and lean classes, and provides a flexible and uncoupled way to bring these behaviors back together.
#
class DiscountCalculator:

    def calculate(self, budget: Budget) -> float:
        # Chains the results
        result = ByFiveItems(
            GraterThanFiveHundred(
                WithoutDiscount()
            )
        ).calculate(budget)

        return round(result, 2)
