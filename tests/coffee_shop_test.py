import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop = CoffeeShop(
            'Little Vienna',
            0.00,
            [
                Drink('Espresso', 3.00),
                Drink('Tea', 2.00),
                Drink('Mocha', 3.50),
                Drink('Latte', 4.25)
            ])
    
    def test_initialization(self):
        self.assertEqual('Little Vienna', self.coffee_shop.name)
        self.assertEqual(0, self.coffee_shop.till)
        self.assertEqual(4, len(self.coffee_shop.drinks))

        