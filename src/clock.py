import pygame


class Clock:
    '''used for control time so game speed is the same in different computers'''
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        self._clock.tick(fps)
