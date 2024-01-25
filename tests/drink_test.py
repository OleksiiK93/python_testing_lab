import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Americano", 3.5, 120)
    
    def test_initialization(self):
        self.assertEqual("Americano", self.drink.name)
        self.assertEqual(3.50, self.drink.price)
        self.assertEqual(120, self.drink.caffeine_level)
        