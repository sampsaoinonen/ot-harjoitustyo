import pygame
import sys, time
from ui.button import Button
from ui.text_box import TextBox
from database.user_repository import UserRepository

class Menu():
    def __init__(self, display):
        self.display = display
        self.bg = pygame.image.load("src/assets/snake_wallpaper.png")
        self.name = ""
        self.user_repository = UserRepository()
        self.speed = 10

    def start_screen(self):        
        self.jake_button = Button(320, 50,  "src/assets/jake.jpg", "src/assets/jake_off.jpg")
        self.play_button = Button(320, 200,  "src/assets/play_off.jpg", "src/assets/play.jpg")
        self.highscore_button = Button(320, 240, "src/assets/highscore_off.jpg", "src/assets/highscore.jpg")
        self.options_button = Button(320, 280, "src/assets/options_off.jpg", "src/assets/options.jpg")
        self.instructions_button = Button(320, 320, "src/assets/instructions_off.jpg", "src/assets/instructions.jpg")
        self.text_box = TextBox(220, 140, 190, 33)

        while True:
            self.display.fill((0,0,0))
            self.display.blit(self.bg, (0, 0))
            self.add_text(20, "Write you name:", 40, 150, (50, 20, 100))
            self.text_box.draw(self.display)

            '''clicking a button with mouse handled here'''
            if self.jake_button.draw(self.display):
                break
            if self.play_button.draw(self.display):
                break
            if self.highscore_button.draw(self.display):
                self.highscore_screen(None)
            if self.options_button.draw(self.display):
                self.options_screen()
            if self.instructions_button.draw(self.display):
                self.instructions_screen()

            '''Keyboard events are handled here'''
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
                        if len(self.name) < 15:
                            self.text_box.write_text(event.unicode)
                            self.name = self.text_box.text
            pygame.display.update()

    def highscore_screen(self, score):
        self.display.fill((0,0,0))
        self.display.blit(self.bg, (0, 0))

        if self.user_repository.check_score(self.name, score):
            self.add_text(30, "Congratulations! You are one of the best!", 40, 10, (255, 0, 0))

        self.add_text(40, "TOP 5", 250, 50, (255, 255, 255))
        self.main_button =  Button(320, 400,  "src/assets/main_off.jpg", "src/assets/main.jpg")

        self.display_topfive()
            

        while True:
            if self.main_button.draw(self.display):
                return False
            
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    return False
            pygame.display.update()

    def options_screen(self):
        self.display.fill((0,0,0))
        self.display.blit(self.bg, (0, 0))
        self.add_text(50, "Set game speed:", 100, 50, (255, 255, 0))

        self.slow_button =  Button(100, 150,  "src/assets/slow_off.jpg", "src/assets/slow.jpg")
        self.normal_button = Button(250, 150, "src/assets/normal_off.jpg", "src/assets/normal.jpg")
        self.fast_button =  Button(400, 150, "src/assets/fast_off.jpg", "src/assets/fast.jpg")
        self.fastest_button =  Button(550, 150, "src/assets/fastest_off.jpg", "src/assets/fastest.jpg")

        while True:
            ''' changing the game speed'''
            if self.slow_button.draw(self.display):
                self.speed = 5
                return False
            if self.normal_button.draw(self.display):
                self.speed = 10
                return False
            if self.fast_button.draw(self.display):
                self.speed = 15
                return False
            if self.fastest_button.draw(self.display):
                self.speed = 20
                return False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
            pygame.display.update()
    
    def instructions_screen(self):
        self.display.fill((0,0,0))
        self.display.blit(self.bg, (0, 0))

        self.add_text(18, "This is a replica of the classic snake game well known from old Nokia phones.", 15, 20, (255, 255, 255))
        self.add_text(18, "Snake can be moved using arrow keys. It’s simple to play - just eat the apples", 15, 40, (255, 255, 255))
        self.add_text(18, "and don’t hit the walls or yourself. The snake grows every time it eats an apple.", 15, 60, (255, 255, 255))
        self.add_text(18, "Game speed can be adjusted from options. Good luck eating them apples!", 15, 80, (255, 255, 255))        

        self.main_button =  Button(320, 400,  "src/assets/main_off.jpg", "src/assets/main.jpg")

        while True:
            if self.main_button.draw(self.display):
                return False
            
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                                return False
            pygame.display.update()

    def end_screen(self, score):
        self.display.fill((0,0,0))
        self.display.blit(self.bg, (0, 0))

        self.add_text(80, "Game Over", 120, 20, (255, 0, 0))
        self.add_text(40, "Your score is: " + str(score), 180, 120, (255, 0, 0))
                                            
        pygame.display.update()
        time.sleep(3)
        self.highscore_screen(score)
        
    def add_text(self, font_size, text, x, y, color):
        font = pygame.font.SysFont('helvetica', font_size)
        disp_text = font.render(text, 1, color)
        self.display.blit(disp_text, (x, y))

    def display_topfive(self):
        topfive = self.user_repository.get_topfive()
        i = 0
        order = 1
        for top in topfive:
            self.add_text(20, str(order) + ". " + top["username"] + "  " + str(top["score"]) + " points", 240, 120 + i, (255, 255, 255))
            i += 30
            order += 1   
