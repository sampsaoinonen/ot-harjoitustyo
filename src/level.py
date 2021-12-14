import pygame
from sprites.snake import Snake
from sprites.snake_tail import SnakeTail
from sprites.apple import Apple

class Level:
    def __init__(self):
        self.snake = Snake()
        self.snake_length = 0
        self.snake_tail_list = []
        self.snake_group = pygame.sprite.Group()
        self.snake_group.add(self.snake)
        self.snake_tail = SnakeTail(self.snake.rect.x, self.snake.rect.y)
        self.snake_tail_group = pygame.sprite.Group()
        self.apple = Apple()
        self.apple_group = pygame.sprite.Group()
        self.apple_group.add(self.apple)
        self.all_sprites = pygame.sprite.Group()  # check if needed
        self.all_sprites.add(
            self.snake_group,
            self.snake_tail_group,
            self.apple_group,
        )

    def move_snake(self, moved_x, moved_y):
        self.snake.rect.move_ip(moved_x, moved_y)

        if self.eaten():
            self.apple_group.empty()
            self.apple = Apple()
            self.apple_group.add(self.apple)
            self.snake_length += 1

    def moving_snake_tail(self):
        snake_tail = SnakeTail(self.snake.rect.x, self.snake.rect.y)
        self.snake_tail_list.append(snake_tail)
        if len(self.snake_tail_list) > self.snake_length:
            self.snake_tail_list.pop(0)
        self.snake_tail_group.empty()
        for tail in self.snake_tail_list:
            self.snake_tail_group.add(tail)

    def eaten(self):
        return pygame.sprite.spritecollide(self.snake, self.apple_group, False)

    def crashed(self, display_width, display_height):
        if (self.snake.rect.x >= display_width or self.snake.rect.x < 0
        or self.snake.rect.y >= display_height or self.snake.rect.y < 0):
            return True
        return pygame.sprite.spritecollide(self.snake, self.snake_tail_group, False)

    def score(self, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render(
            'Score : ' + str(self.snake_length), True, color)
        score_rect = score_surface.get_rect()
        display_width = pygame.display.get_surface().get_size()[0]
        score_rect.midtop = (display_width/10, 10)
        return score_surface, score_rect
