import unittest
from sprites.apple import Apple 

class testSnake(unittest.Testcase):   
    def setUp(self):
        self.apple = Apple()        

    def test_random_x_and_y_is_in_display_and_dividable_by_20(self):        
        self.assertEqual(self.Apple.rect.x, (<1000))
        self.assertEqual(self.Apple.rect.y, (<1000))
