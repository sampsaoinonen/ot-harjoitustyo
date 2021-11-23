import unittest
from sprites.snake import Snake 

class testSnake():   
    def setUp(self):
        self.snake = Snake()        

    def test_konstruktori_asettaa_x_ja_y_arvot(self):        
        self.assertEqual(self.snake.rect.x, 320)
        self.assertEqual(self.snake.rect.x, 240)
            

    

