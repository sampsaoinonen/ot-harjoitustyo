import pygame
import sys, time
from ui.button import Button
from ui.text_box import TextBox

class Menu():
    def __init__(self, display):
        self.display = display
        self.bg = pygame.image.load("src/assets/snake_wallpaper.png")

    def start_screen(self):
        self.play_image = pygame.image.load("src/assets/play.jpg")
        self.play_button = Button(165, 100, self.play_image)
        self.text_box = TextBox(165, 50, 100, 50)
        while True:
            self.display.fill((0,0,0))
            self.display.blit(self.bg, (0, 0))            

            if self.play_button.draw(self.display):
                break
            self.text_box.draw(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return False
                    if event.key == pygame.K_BACKSPACE:
                        self.text_box.erase()
                    else:                        
                        self.text_box.write_text(event.unicode)
            pygame.display.update()
    
    def end_screen(self, score):
        game_over_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = game_over_font.render('Game Over!', True, (255, 0 ,0))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (pygame.display.get_surface().get_size()[0]/2, pygame.display.get_surface().get_size()[1]/8)
        
        score_font = pygame.font.SysFont('times new roman', 40)
        score_surface = score_font.render("Your score is: " + str(score), True, (255, 0 ,0))
        score_rect = score_surface.get_rect()
        score_rect.midtop = (pygame.display.get_surface().get_size()[0]/2, pygame.display.get_surface().get_size()[1]/3)
          
        self.display.fill((0,0,0))
        self.display.blit(self.bg, (0, 0))
        self.display.blit(game_over_surface, game_over_rect)
        self.display.blit(score_surface, score_rect)   
        pygame.display.flip()
        time.sleep(5)

        