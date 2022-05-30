import pygame
from pygame.sprite import Sprite
from settings import Settings


class Button(Sprite):

	def __init__(self,wordle_game):
		super().__init__()
		self.s=Settings()
		self.screen=wordle_game.screen
		self.screen_rect=wordle_game.screen.get_rect()
		self.color=self.s.not_used

		self.width, self.height=self.s.button_width, self.s.button_height
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.x=20
		self.rect.y=355

		self.label=''

		self.font=pygame.font.SysFont(self.s.text_font, self.s.button_font_size)

	def draw_button(self, label):
		pygame.draw.rect(self.screen, self.color, self.rect, 0, 2)
		self.label=label
		text=self.font.render(label, True, self.s.text_color)
		text_rect=text.get_rect(center=self.rect.center)
		self.screen.blit(text, text_rect)
		pygame.display.update()