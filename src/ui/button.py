import pygame

class Button():
	def __init__(self, x, y, image_off, image_on):
		self.image_off = image_off
		self.image_on = image_on				
		self.image = pygame.image.load(image_off)	
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False		

	''' will make image change on and off pics when mouse on'''
	def mouse_on(self, pos):
		if self.rect.collidepoint(pos):
			self.image = pygame.image.load(self.image_on)
		else:
			self.image = pygame.image.load(self.image_off)

	'''checking mouse action and clicked conditions'''
	def mouse_clicked(self, pos, action):
		if self.rect.collidepoint(self.pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				self.action = True
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False	

	def draw(self, surface):
		'''mouse position'''
		self.pos = pygame.mouse.get_pos()
		self.action = False

		'''checking mouse action and clicked conditions'''
		self.mouse_clicked(self.pos, self.action)
			
		self.mouse_on(self.pos)

		'''drawing button on screen'''
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return self.action
