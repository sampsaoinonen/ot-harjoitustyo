"""Pygame module."""
import pygame
from load_image import load_image


class Snake(pygame.sprite.Sprite):
    """ Creates a movable sprite """

    def __init__(self):
        super().__init__()
        self.image = load_image("snake.png")
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = 240

    def move(self, move_x, move_y):
        """ Changes snakes x and y values by move_x and move_y """
        self.rect.move_ip(move_x, move_y)
