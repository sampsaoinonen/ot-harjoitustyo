import pygame
from sprites.snake import Snake
from sprites.snake_tail import Snake_tail
from sprites.apple import Apple




class Level:
    def __init__(self, cell_size):
        self.snake = Snake()
        self.snake_length = 0
        self.snake_tail_list = []
        self.snake_group = pygame.sprite.Group()
        self.snake_group.add(self.snake)
        self.snake_tail = Snake_tail(self.snake.rect.x, self.snake.rect.y)
        self.snake_tail_group = pygame.sprite.Group()
        self.apple = Apple()
        self.apple_group = pygame.sprite.Group()
        self.apple_group.add(self.apple)
        self.all_sprites = pygame.sprite.Group() # check if needed
        self.all_sprites.add(
            self.snake_group,
            self.snake_tail_group,
            self.apple_group,            
        )
        
    def move_snake(self, dx, dy):
        self.snake.rect.move_ip(dx, dy)
        self.update()
        
        if (self.eaten()):                        
            self.apple_group.empty()
            self.apple = Apple()
            self.apple_group.add(self.apple)
            self.snake_length += 1
            

            

    def moving_snake_tail():
        snake_tail = Snake_tail(self.snake.rect.x, self.snake.rect.y)
        self.snake_tail_list.append(self.snake_tail)
        if len(self.snake_tail_list) > self.snake_length:
            self.snake_tail_list.pop(0)    

        self.snake_tail_group.empty()
        for tail in self.snake_tail_list:    
            self.snake_tail_group.add(tail) 
        

    def eaten(self): 
        return pygame.sprite.spritecollide(self.snake, self.apple_group, False)

    def update(self):
        self.snake_group.update()
        self.apple_group.update()
