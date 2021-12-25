import pygame

class TextBox():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y    
        self.text = ""
        self.border = False
        self.image = pygame.Surface((width, height))    
        self.font = pygame.font.SysFont("helvetica", 18)

    def draw(self, surface):
        self.image.fill((250,250,250))
        text = self.font.render(self.text, False, (100,100,100))
        self.image.blit(text, (15,15))
        surface.blit(self.image, (self.x, self.y))

    def write_text(self, un):
        self.text += un

    def erase(self):
        self.text = self.text[:-1]
