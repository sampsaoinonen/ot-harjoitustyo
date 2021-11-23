import pygame, sys, random
from sprites.snake import Snake
from sprites.apple import Apple
    
        
pygame.init()
clock = pygame.time.Clock() 
CELL_SIZE = 5
BG_COLOR = (0,0,0)


display_width = 640
display_height = 480
display = pygame.display.set_mode((display_width, display_height))
#background = pygame.image.load("grass.png")


snake = Snake()
snake_group = pygame.sprite.Group()
snake_group.add(snake)
x_change = 0 
y_change = 0

apple = Apple()
apple_group = pygame.sprite.Group()
apple_group.add(apple)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (-CELL_SIZE) 
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (CELL_SIZE)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (-CELL_SIZE)
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (CELL_SIZE)

    eaten = pygame.sprite.spritecollide(snake, apple_group, False)        
    if(eaten):            
        apple = Apple()
        apple_group.empty()
        apple_group.add(apple)      
    snake.move(x_change, y_change)    
    pygame.display.flip()
    display.fill(BG_COLOR)
    #display.blit(background,(0,0))
    snake_group.draw(display)
    apple_group.draw(display)
    
    
    
    clock.tick(60)
    
