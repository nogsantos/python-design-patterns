# -*- coding: utf-8 -*-
from unittest import TestCase

from src.chain_of_responsibility.item import Item
from src.chain_of_responsibility.discount_calculator import DiscountCalculator, Budget


class TestChainOfResponsibility(TestCase):

    def setUp(self):
        self.budget = Budget()

    def test_budget_it_should_calculate_the_total_of_items_values(self):
        self.budget.add(Item('Item #1', 100.0))
        self.budget.add(Item('Item #2', 100.0))
        self.budget.add(Item('Item #3', 100.0))

        self.assertEqual(self.budget.total, 300.0)

    def test_budget_it_should_get_a_tuple_of_items(self):
        self.budget.add(Item('Item #1', 100.0))

        self.assertEqual(type(self.budget.items), tuple)

    def test_budget_it_should_get_the_length_of_items(self):
        self.budget.add(Item('Item #1', 100.0))
        self.budget.add(Item('Item #2', 100.0))

        self.assertEqual(self.budget.items_len, 2)

    def test_budget_it_should_add_items_to_the_list(self):
        self.budget.add(Item('Item #1', 100.0))
        self.assertEqual(self.budget.items_len, 1)

        self.budget.add(Item('Item #2', 100.0))
        self.assertEqual(self.budget.items_len, 2)

    def test_discount_it_should_calculate_the_budget_discount_when_the_budget_has_more_than_five_items(self):
        self.budget.add(Item('Item #1', 100.0))
        self.budget.add(Item('Item #2', 100.0))
        self.budget.add(Item('Item #3', 100.0))
        self.budget.add(Item('Item #4', 100.0))
        self.budget.add(Item('Item #5', 100.0))
        self.budget.add(Item('Item #6', 100.0))
        self.budget.add(Item('Item #7', 100.0))
        self.budget.add(Item('Item #8', 100.0))
        self.budget.add(Item('Item #9', 100.0))
        self.budget.add(Item('Item #10', 100.0))

        calculator = DiscountCalculator()

        discount = calculator.calculate(self.budget)

        self.assertEqual(discount, 100.0)

    def test_discount_it_should_calculate_the_budget_discount_when_the_budget_has_less_than_five_items_but_the_value_is_more_than_five_hundred(
            self):
        self.budget.add(Item('Item #1', 100.0))
        self.budget.add(Item('Item #2', 50.0))
        self.budget.add(Item('Item #3', 400.0))

        calculator = DiscountCalculator()

        discount = calculator.calculate(self.budget)

        self.assertEqual(discount, 38.50)

    def test_discount_it_should_had_no_discount_value(self):
        self.budget.add(Item('Item #1', 100.0))
        self.budget.add(Item('Item #2', 100.0))
        self.budget.add(Item('Item #3', 300.0))

        calculator = DiscountCalculator()

        discount = calculator.calculate(self.budget)

        self.assertEqual(discount, 0.0)
