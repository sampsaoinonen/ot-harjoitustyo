import pygame


class TextBox():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = ""
        #self.text_font = pygame.font.Sysfont('helvetica', 20)
        self.border = False
        self.image = pygame.Surface((180, 50))
        pygame.font.init()
        self.font = pygame.font.SysFont("helvetica", 18)
    
    
    def draw(self, surface):
        self.image.fill((250,250,250))
        text = self.font.render(self.text, False, (100,100,100))
        self.image.blit(text, (15,15))
        surface.blit(self.image, (220, 40))
        action = False
        
    def write_text(self, un):        
        self.text += un           
        
    
    def erase(self):
        self.text = self.text[:-1]