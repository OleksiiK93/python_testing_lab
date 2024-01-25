import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Oleksii", 13.00)
    
    def test_initialization(self):
        self.assertEqual("Oleksii", self.customer.name)
        self.assertEqual(13.00, self.customer.wallet)
    
    def test_wallet_can_be_reduced_by_amount(self):
        self.customer.reduce_wallet(2.0)
        self.assertEqual(11.00, self.customer.wallet)
    
    def test_customer_can_buy_drink(self):
        drink = Drink("Americano", 3.5)
        self.customer.buy_drink(drink)
        self.assertEqual(9.5, self.customer.wallet)