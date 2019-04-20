# -*- coding: utf-8 -*-

from src.strategy.budget import Budget


#
# Strategy:
#
#   The Strategy pattern gives us a flexible way to write several different algorithms,
#   and pass these algorithms to client classes that need them.
#   These clients are unaware of what the "real" algorithm is running,
#   and just tells the algorithm to run. This causes the client class code to be quite
#   decoupled from the implementations of the algorithms, thus enabling this client to be able to
#   work with N different algorithms without having to change its code.
#
class TaxCalculator:

    # Using duck type to pass the tax calculate method
    def calculate(self, budget: Budget, tax) -> float:
        return tax.calculate(budget)
