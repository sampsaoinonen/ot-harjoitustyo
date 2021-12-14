import pygame
from level import Level
from game_loop import GameLoop
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock
from ui.menu import Menu

CELL_SIZE = 20
BG_COLOR = (0, 0, 0)

def main():
    display_width = 640
    display_height = 480
    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("JakeTheSnake")

    level = Level()
    menu = Menu(display)
    event_queue = EventQueue()
    renderer = Renderer(display, level, BG_COLOR)
    clock = Clock()
    game_loop = GameLoop(level, renderer, event_queue,
                         clock, CELL_SIZE, display_width, display_height)

    while True:
        pygame.init()
        menu.start_screen()
        game_loop.start()
        menu.end_screen(level.snake_length)
        return False

if __name__ == "__main__":
    main()
