"""Pygame module."""
import pygame
from load_image import load_image

class Snake_tail(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.parts = []
        self.image = load_image("body.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
