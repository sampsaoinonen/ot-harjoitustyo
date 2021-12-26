import pygame


class Renderer:
    '''controls drawing everything on the screen'''
    def __init__(self, display, level, bg_color):
        self._display = display
        self._level = level
        self._bg_color = bg_color

    def render(self):
        self._display.fill(self._bg_color)
        self._level.snake_group.draw(self._display)
        self._level.apple_group.draw(self._display)
        self._level.snake_tail_group.draw(self._display)
        score = self._level.score(pygame.Color(255, 255, 255), 'helvetica', 20)
        self._display.blit(score[0], score[1])
        pygame.display.update()
