''''''
import os
import pygame

dirname = os.path.dirname(__file__)

def load_image(filename):
    ''''creates a path to images in assets dir'''
    return pygame.image.load(
        os.path.join(dirname, "assets", filename)
    )
