import unittest
from sprites.snake_tail import SnakeTail


class testSnake(unittest.TestCase):
    def setUp(self):
        self.snake_tail = SnakeTail(100, 100)

    def test_constructor_sets_up_x_and_y(self):
        self.assertEqual(self.snake_tail.rect.x, 100)
        self.assertEqual(self.snake_tail.rect.y, 100)
