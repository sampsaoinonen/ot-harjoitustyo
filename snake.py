import pygame


class Snake(pygame.sprite.Sprite):   
    def __init__(self):
        super().__init__()        
        self.image = pygame.image.load("snake.png")
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = 240
            
    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)

    def colliding_walls(self):
        pass

    
 
