# -*- coding: utf-8 -*-

from src.taxes.tax_calculator import TaxCalculator
from src.taxes.budget import Budget
from src.taxes.tax import ICMS, ISS

calculator = TaxCalculator()
budget = Budget(500)

iss = calculator.calculate(budget, ISS())
icms = calculator.calculate(budget, ICMS())

print(f'Budget: {budget.value}\nISS: {iss}\nICMS: {icms}')
