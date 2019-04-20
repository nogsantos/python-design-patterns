# -*- coding: utf-8 -*-
from unittest import TestCase

from src.taxes.budget import Budget
from src.taxes.tax import ICMS, ISS
from src.taxes.tax_calculator import TaxCalculator


class TestTaxCalculator(TestCase):

    def setUp(self):
        self.budget = Budget(500)
        self.calculator = TaxCalculator()

    def test_calculate_iss_tax_value(self):
        iss = self.calculator.calculate(self.budget, ISS())
        self.assertEqual(50.0, iss)

    def test_calculate_icms_tax_value(self):
        icms = self.calculator.calculate(self.budget, ICMS())

        self.assertEqual(30.0, icms)
