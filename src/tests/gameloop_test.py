import unittest
import pygame

from level import Level
from game_loop import GameLoop
from sprites.snake import Snake


class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        0


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def render(self):
        pass


display_width = 640
display_height = 480
cell_size = 320
'''cell_size means how much the snake moves with one keydown. If snakes starting position
is 320.240 by default then 320 to the right will hit the wall''


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.level = Level()        
        
    def test_can_complete_level(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_RIGHT),
        ]

        game_loop = GameLoop(
            self.level,
            StubRenderer(),
            StubEventQueue(events),
            StubClock(),
            cell_size,
            display_width,
            display_height
        )
        
        pygame.init()
        game_loop.start()        
        self.assertTrue(self.level.crashed(display_width, display_height))

