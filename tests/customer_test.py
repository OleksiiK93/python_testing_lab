import unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food
from src.coffee_shop import CoffeeShop

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Oleksii", 13.00, 15)
        self.coffee_shop = CoffeeShop(
            'Little Vienna',
            0.00,
            {
                'espresso': {
                    'info': Drink('Espresso', 3.00, 65),
                    'amount': 100
                    },
                'tea': {
                    'info': Drink('Tea', 2.00, 50),
                    'amount': 150
                    },
                'americano': {
                    'info': Drink('Americano', 3.50, 130),
                    'amount': 100
                    },
                'latte': {
                    'info': Drink('Latte', 4.25, 65),
                    'amount': 180
                    }
            })
    
    def test_initialization(self):
        self.assertEqual("Oleksii", self.customer.name)
        self.assertEqual(13.00, self.customer.wallet)
        self.assertEqual(15, self.customer.age)
        self.assertEqual(0, self.customer.energy)
    
    def test_wallet_can_be_reduced_by_amount(self):
        self.customer.reduce_wallet(2.0)
        self.assertEqual(11.00, self.customer.wallet)
    
    def test_customer_can_buy_drink(self):
        self.customer.buy_drink(self.coffee_shop.drinks['americano'])
        self.assertEqual(9.5, self.customer.wallet)
        self.assertEqual(130, self.customer.energy)
    
    def test_customer_can_buy_food(self):
        food = Food("Carrot Cake", 5.0, 100)
        self.customer.buy_food(food)
        self.assertEqual(8.0, self.customer.wallet)
        self.assertEqual(-100, self.customer.energy)