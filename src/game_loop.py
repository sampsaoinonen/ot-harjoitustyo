import pygame


class GameLoop:
    def __init__(self, level, renderer, event_queue, clock, cell_size, BG_COLOR, display):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size
        self._direction = ""
        self._x_change = 0
        self._y_change = 0
        self._BG_COLOR = BG_COLOR
        self._display = display
        

    def start(self):
        while True:
            if self._handle_events() == False:
                break

            self._level.update()
            self._render()                        
            self._level.move_snake(self._x_change, self._y_change)            
            self._clock.tick(10)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:                
                if event.key == pygame.K_LEFT and self._direction != "right": #lets make sure snake cannot turn the opposite direction
                    self._x_change = (-self._cell_size) 
                    self._y_change = 0                    
                    self._direction = "left"
                if event.key == pygame.K_RIGHT and self._direction != "left":
                    self._x_change = (self._cell_size)
                    self._y_change = 0
                    self._direction = "right"
                if event.key == pygame.K_UP and self._direction != "down":
                    self._x_change = 0
                    self._y_change = (-self._cell_size)
                    self._direction = "up"
                if event.key == pygame.K_DOWN and self._direction != "up":
                    self._x_change = 0
                    self._y_change = (self._cell_size)
                    self._direction = "down"                                         
                
            elif event.type == pygame.QUIT:
                return False                        

    def _render(self):
        self._renderer.render()
