import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Oleksii", 13.00)
    
    def test_initialization(self):
        self.assertEqual("Oleksii", self.customer.name)
        self.assertEqual(13.00, self.customer.wallet)
    
    def test_wallet_can_be_reduced_by_amount(self):
        self.customer.reduce_wallet(2.0)
        self.assertEqual(11.00, self.customer.wallet)