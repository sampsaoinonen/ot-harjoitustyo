import unittest
from snake import Snake 

class testSnake(unittest.TestCase):   
    def setUp(self):
        self.snake = Snake()        

    def test_constructor_sets_up_x_and_y(self):        
        self.assertEqual(self.snake.rect.x, 320)
        self.assertEqual(self.snake.rect.y, 240)
            

    

