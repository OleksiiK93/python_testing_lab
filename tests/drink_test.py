import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Americano", 3.5)
    
    def test_initialization(self):
        self.assertEquals("Americano", self.drink.name)
        self.assertEquals(3.50, self.drink.price)
        