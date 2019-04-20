# -*- coding: utf-8 -*-

from src.strategy.budget import Budget


class ISS:

    def calculate(self, budget: Budget) -> float:
        return budget.value * 0.1


class ICMS:

    def calculate(self, budget: Budget) -> float:
        return budget.value * 0.06
