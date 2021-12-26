import pygame

class GameLoop:
    '''Sets up every thing needed to run an event loop'''

    def __init__(self, level, renderer, event_queue, clock, cell_size, display_width, display_height):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size
        self._direction = ""
        self._x_change = 0
        self._y_change = 0
        self._display_width = display_width
        self._display_height = display_height

    def start(self, game_speed):
        while True:
            self._level.moving_snake_tail()
            if self._handle_events() is False:
                break
            self._level.move_snake(self._x_change, self._y_change)
            self._level.eaten()

            self._render()

            if self._level.crashed(self._display_width, self._display_height):
                return False

            self._clock.tick(game_speed)

    def _handle_events(self):
        '''changes a key pressed down to direction for snake'''
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                ''' lets make sure snake cannot turn the opposite direction '''
                if event.key == pygame.K_LEFT and self._direction != "right":
                    self._x_change = -self._cell_size
                    self._y_change = 0
                    self._direction = "left"
                if event.key == pygame.K_RIGHT and self._direction != "left":
                    self._x_change = self._cell_size
                    self._y_change = 0
                    self._direction = "right"
                if event.key == pygame.K_UP and self._direction != "down":
                    self._x_change = 0
                    self._y_change = -self._cell_size
                    self._direction = "up"
                if event.key == pygame.K_DOWN and self._direction != "up":
                    self._x_change = 0
                    self._y_change = self._cell_size
                    self._direction = "down"

            elif event.type == pygame.QUIT:
                return False
        

    def _render(self):
        self._renderer.render()
