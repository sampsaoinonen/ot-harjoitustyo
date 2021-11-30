import pygame, sys, random, time
from sprites.snake import Snake
from sprites.apple import Apple
from sprites.snake_tail import Snake_tail
    
        
pygame.init()
clock = pygame.time.Clock() 
CELL_SIZE = 20
BG_COLOR = (0,0,0)
white = pygame.Color(255, 255, 255)


display_width = 640
display_height = 480
display = pygame.display.set_mode((display_width, display_height))
#background = pygame.image.load("grass.png")


snake = Snake()
snake_group = pygame.sprite.Group()
snake_group.add(snake)
x_change = 0 
y_change = 0
direction = ""


apple = Apple()
apple_group = pygame.sprite.Group()
apple_group.add(apple)

snake_tail = Snake_tail(snake.rect.x, snake.rect.y)
snake_tail_group = pygame.sprite.Group()

snake_tail_list = []
snake_length = 0

def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('Game Over!', True, (255, 0 ,0))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (display_width/2, display_height/4)
    display.fill(BG_COLOR)
    display.blit(game_over_surface, game_over_rect)    
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

def score(points, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(points), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (display_width/10, 10)    
    display.blit(score_surface, score_rect)
    
while True:

    
    snake_tail = Snake_tail(snake.rect.x, snake.rect.y)
    snake_tail_list.append(snake_tail)
    if len(snake_tail_list) > snake_length:
        snake_tail_list.pop(0)    

    snake_tail_group.empty()
    for tail in snake_tail_list:    
        snake_tail_group.add(tail)            
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()                

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "right": #lets make sure snake cannot turn the opposite direction
                x_change = (-CELL_SIZE) 
                y_change = 0
                direction = "left"
            if event.key == pygame.K_RIGHT and direction != "left":
                x_change = (CELL_SIZE)
                y_change = 0
                direction = "right"
            if event.key == pygame.K_UP and direction != "down":
                x_change = 0
                y_change = (-CELL_SIZE)
                direction = "up"
            if event.key == pygame.K_DOWN and direction != "up":
                x_change = 0
                y_change = (CELL_SIZE)
                direction = "down"    
    if (snake.rect.x >= display_width or snake.rect.x < 0 or snake.rect.y >= display_height or snake.rect.y < 0):                       
        game_over()            
    
    eaten = pygame.sprite.spritecollide(snake, apple_group, False)        
    if(eaten):            
        apple = Apple()
        apple_group.empty()
        apple_group.add(apple)
        snake_length += 1
        
    snake.move(x_change, y_change)    
    pygame.display.flip()
    display.fill(BG_COLOR)    
    snake_group.draw(display)
    apple_group.draw(display)
    snake_tail_group.draw(display)
    score(snake_length, white, 'helvetica', 20)

    collide_itself = pygame.sprite.spritecollide(snake, snake_tail_group, False)
    if(collide_itself):
        game_over()


    
    
    clock.tick(10)





