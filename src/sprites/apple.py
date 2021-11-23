import pygame, random

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple.png")  #size of pic is 40
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 640-30)
        self.rect.y = random.randint(0, 480-30)
