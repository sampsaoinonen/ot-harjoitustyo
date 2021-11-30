import pygame
from load_image import load_image

class Snake_tail(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.parts = []
        self.image = load_image("body.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
        

    
