import pygame

class Snake_tail(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.parts = []
        self.image = pygame.image.load("body.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
        

    
