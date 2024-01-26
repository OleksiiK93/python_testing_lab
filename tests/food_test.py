import unittest
from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food("Carrot Cake", 5.0, 100)
    
    def test_initialization(self):
        self.assertEqual("Carrot Cake", self.food.name)
        self.assertEqual(5.0, self.food.price)
        self.assertEqual(100, self.food.digestion_level)