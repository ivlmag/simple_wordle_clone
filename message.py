import pygame
from pygame.sprite import Sprite
from settings import Settings


class Message(Sprite):

	def __init__(self,wordle_game):
		super().__init__()
		self.s=Settings()
		self.screen=wordle_game.screen
		self.screen_rect=wordle_game.screen.get_rect()
		self.color=self.s.bg

		self.width, self.height=self.s.screen_width, self.s.box_size
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.centerx=self.screen_rect.centerx
		self.rect.y=70

		self.font=pygame.font.SysFont(self.s.text_font, self.s.text_size)
		self.message=""
		self.text=self.font.render(self.message, True, self.s.text_color)
		self.text.set_alpha(self.s.full)

	def draw_msg(self):
		self.screen.fill(self.color,self.rect)

	def add_msg(self, message_text, is_alpha):
		self.message=message_text
		self.text=self.font.render(self.message, True, self.s.text_color)
		text_rect=self.text.get_rect(center=self.rect.center)
		self.text.set_alpha(is_alpha)
		self.screen.blit(self.text, text_rect)
		pygame.display.update()

	def fade(self):
		alpha=self.text.get_alpha()
		self.draw_msg()
		self.add_msg(self.message, is_alpha=(alpha-5))
