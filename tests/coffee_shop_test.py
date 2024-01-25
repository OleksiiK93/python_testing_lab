import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop = CoffeeShop(
            'Little Vienna',
            0.00,
            [
                Drink('Espresso', 3.00, 65),
                Drink('Tea', 2.00, 50),
                Drink('Americano', 3.50, 130),
                Drink('Latte', 4.25, 65)
            ])
        self.customer = Customer("Oleksii", 13.00, 30)
    
    def test_initialization(self):
        self.assertEqual('Little Vienna', self.coffee_shop.name)
        self.assertEqual(0, self.coffee_shop.till)
        self.assertEqual(4, len(self.coffee_shop.drinks))

    def test_can_sell_drink_to_customer(self):
        self.coffee_shop.sell(self.coffee_shop.drinks[0], self.customer)
        self.assertEqual(3.0, self.coffee_shop.till)
        self.assertEqual(10, self.customer.wallet)

    def test_does_not_sell_coffee_to_minors(self):
        customer = Customer("Andrew", 100.0, 15)
        self.coffee_shop.sell(self.coffee_shop.drinks[0], customer)
        self.assertEqual(0, self.coffee_shop.till)

    def test_does_not_sell_to_customers_with_energy_above_100(self):
        self.coffee_shop.sell(self.coffee_shop.drinks[2], self.customer)
        self.coffee_shop.sell(self.coffee_shop.drinks[2], self.customer)
        self.assertEqual(3.5, self.coffee_shop.till)