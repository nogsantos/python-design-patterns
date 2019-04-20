# -*- coding: utf-8 -*-

from src.strategy.tax_calculator import TaxCalculator
from src.strategy.budget import Budget
from src.strategy.tax import ICMS, ISS

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

calculator = TaxCalculator()
budget = Budget(500)

iss = calculator.calculate(budget, ISS())
icms = calculator.calculate(budget, ICMS())

print(f'Budget: {budget.value}\nISS: {iss}\nICMS: {icms}')
