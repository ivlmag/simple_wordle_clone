import pygame
from pygame.sprite import Sprite
from settings import Settings


class Box(Sprite):

	def __init__(self,wordle_game):
		super().__init__()
		self.s=Settings()
		self.screen=wordle_game.screen
		self.screen_rect=wordle_game.screen.get_rect()
		self.color=self.s.bg

		self.width, self.height=self.s.box_size, self.s.box_size
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.x=20
		self.rect.y=105

		self.border_color=self.s.grey

		self.font=pygame.font.SysFont(self.s.text_font, self.s.box_font_size)

	def draw_box(self, color, bord_color):
		pygame.draw.rect(self.screen, color, self.rect, 0)
		pygame.draw.rect(self.screen, bord_color, self.rect, 1)

	def add_text(self, text):
		text=self.font.render(text, True, self.s.text_color)
		text_rect=text.get_rect(center=self.rect.center)
		self.screen.blit(text, text_rect)
		pygame.display.update()