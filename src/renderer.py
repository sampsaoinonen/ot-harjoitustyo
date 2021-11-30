import pygame


class Renderer:
    def __init__(self, display, level, BG_COLOR):
        self._display = display
        self._level = level
        self._BG_COLOR = BG_COLOR

    def render(self):
        self._display.fill(self._BG_COLOR)        
        self._level.snake_group.draw(self._display)
        self._level.apple_group.draw(self._display)
        self._level.snake_tail_group.draw(self._display)
        pygame.display.update()
