"""Pygame module."""
import pygame
from load_image import load_image


class SnakeTail(pygame.sprite.Sprite):
    '''Sets up snaketail wich is the length our snake grows every time it eats an apple'''

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.parts = []
        self.image = load_image("body.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
