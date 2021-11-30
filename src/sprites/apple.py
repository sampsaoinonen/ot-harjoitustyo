import pygame, random
from load_image import load_image


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("apple.png")         
        self.rect = self.image.get_rect()
                
        self.rect.x = random.randrange(0, 640-20, 20)
        self.rect.y = random.randrange(0, 480-20, 20)
        

        #here something to prevent apple appear under tail

