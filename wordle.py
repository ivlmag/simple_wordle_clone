import sys
import string
import random

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.sprite import Sprite

from checker import check_wordle
from settings import Settings
from box import Box
from message import Message
from button import Button


class Wordle:

	def __init__(self):
		pygame.init()
		self.s=Settings()

		self.screen=pygame.display.set_mode((self.s.screen_width,
											self.s.screen_height))

		programIcon = pygame.image.load('wordle-game-icon-512.png')
		pygame.display.set_icon(programIcon)

		self.font=pygame.font.SysFont(self.s.text_font, self.s.text_size)
		self.text=self.font.render('',True,self.s.text_color)

		self.screen.fill(self.s.bg)

		pygame.display.set_caption("Wordle")
		self.show_logo()

		self.attempt=0
		self.current_box=0

		self.index=0
		self.can_print=True

		self.guess=[]
		self.run_game=True

		self.boxes=pygame.sprite.Group()
		self.create_boxes()

		self.message=Message(self)

		self.buttons=pygame.sprite.Group()
		self.create_buttons()

		self.timer=0

		self.color_dict={'G':self.s.green, 'Y':self.s.yellow, 'W':self.s.grey}

	def run(self):		
		while True:

			'''Index of the current box in entire boxes group (30 total)'''
			self.index=self.attempt*5+self.current_box

			self.check_key()			
			self.screen_rect=self.screen.get_rect()
			self.fade_message()
			pygame.display.flip()

	def fade_message(self):
		'''Fading message'''
		if self.run_game:
			self.timer+=1
			if self.timer>self.s.timer_length:
				self.message.fade()
				self.timer=0

	def check_key(self):
		'''Checking input from player'''
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			elif event.type==pygame.KEYDOWN and self.run_game:
				if event.key == pygame.K_BACKSPACE:
					self.backspace()
				elif event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
					self.enter()
				elif pygame.key.name(event.key) in list(string.ascii_lowercase):
					self.new_letter(letter=pygame.key.name(event.key))
			elif event.type==pygame.MOUSEBUTTONDOWN and self.run_game:
				self.check_button_click(pygame.mouse.get_pos())

	def check_button_click(self, mouse_pos):
		'''Check if mouse was clicked on any button'''
		for button in self.buttons:
			if button.rect.collidepoint(mouse_pos):
				if button.label=='DEL':
					self.backspace()
				elif button.label=='ENTER':
					self.enter()
				else:
					self.new_letter(button.label.lower())
	
	def backspace(self):
		'''Clearing the box'''
		if ((self.current_box==4 and not self.can_print)
			or self.current_box==0):
			'''If filled last box or first box, 
			clear it but stay in the box'''
			self.delete_letter(self.index)
		elif self.current_box>0:
			'''If not first box or empty last box,
			go back one box and clear it'''
			self.current_box-=1
			self.delete_letter(self.index-1)

	def delete_letter(self, index):
		'''To delete a letter, get the box by index, 
		empty the text in box and repaint. Delete from guess if not empty. 
		Now can print in it (important for last box only)'''
		edit_box=self.get_box(index)
		edit_box.add_text('')
		edit_box.draw_box(color=self.s.bg, bord_color=self.s.grey)
		if self.guess:
			self.guess.pop()
		self.can_print=True

	def new_letter(self, letter):
		if self.current_box<=4 and self.can_print:
			'''If letter is pressed and there is place to add letter,
			add letter and repaint the box'''
			edit_box=self.get_box(self.index)
			edit_box.draw_box(color=self.s.bg, bord_color=self.s.not_used)
			edit_box.add_text(letter.upper())
			self.guess.append(letter)
			'''If not last box in line, go to the next.
			If the box is last - don't allow to add more symbols'''
			if self.current_box!=4:
				self.current_box+=1
			else:
				self.can_print=False

	def enter(self):
		'''If line is full and word exists,
		checking the answer, painting leters and going to the next attempt'''
		if (len(self.guess)==5 and 
			''.join(self.guess) in words):
			result=random.choice(check_wordle(word, self.guess)) #Checking
			self.paint_result(result) #Painting letters
			if result==['G']*5:	#Victory						
				self.show_message(self.s.messages[(self.attempt+1)], 
									is_alpha=self.s.full)
				self.run_game=False
			elif self.attempt==5: #User didn't guess the word in 6 attempts
				self.show_message(f'The word was "{word}"', is_alpha=self.s.full)
				self.run_game=False
			else: #Clearing messagebox and going to the next attempt, if possible
				self.show_message('', is_alpha=self.s.full)
				if self.attempt<=4:
					self.attempt+=1
					self.current_box=0
					self.can_print=True
					self.guess=[]
		else: #Word is too short or doesn't exist
			self.show_message("Can't use this word", is_alpha=self.s.transparent)

	def get_box(self, index):
		'''Using the index in boxes group (30 total),
		return a box for editing'''
		return self.boxes.sprites()[index]

	def paint_result(self, result):
		for i in range(4, -1, -1):
			'''For every symbol in result, repaint boxes and buttons'''
			edit_box=self.get_box(self.index-i)
			color=self.color_dict[result[4-i]]
			edit_box.draw_box(color, color)
			letter=self.guess[4-i].upper()
			edit_box.add_text(letter)
			self.paint_button(letter, color)

	def paint_button(self,letter,color):
		def _repaint():
			button.color=color
			button.draw_button(button.label)

		'''If button already green - don't repaint
		If button yellow - repaint only if in new guess the position is green'''
		for button in self.buttons:
			if button.label==letter.upper():
				if color==self.s.green:
					_repaint()
				elif button.color!=self.s.green and color==self.s.yellow:
					_repaint()
				elif button.color!=self.s.green and button.color!=self.s.yellow:
					_repaint()

	def show_message(self, message_text, is_alpha):
		'''First function refills messagebox with standart background color,
		second adds message_text and sets alpha level for transparent message'''
		self.message.draw_msg()
		self.message.add_msg(message_text, is_alpha)

	def draw_box(self):
		'''Displaying the boxes'''
		self.screen.fill(self.color,self.rect)

	def show_logo(self):
		'''Painting logo WORDLE'''
		font=pygame.font.Font(self.s.logo_font, self.s.logo_size)
		text=font.render('Wordle',True,self.s.text_color)
		rect=text.get_rect()
		self.screen_rect=self.screen.get_rect()
		rect.centerx=self.screen_rect.centerx
		rect.centery=40
		self.screen.blit(text,rect)

	def create_boxes(self):
		'''Creating and arranging 30 boxes for input'''
		for row_number in range(0,6):
			for box_number in range(0,5):
				box=Box(self)
				box_width,box_height=box.rect.size

				'''Calculating k - multiplier to arrange boxes evenly, 
				depending on the game window width'''
				screen_width=self.screen.get_rect().width
				k=(screen_width-2*20)/(5*box_width)
				box.x=k*(20+box_width*box_number)
				box.rect.x=box.x

				'''Calculating the space between boxes, 
				so it can be symmetrically used as a divider between rows'''
				diff=(screen_width-2*20-5*box_width)/5 
				box.rect.y=105+row_number*(box_height+4)

				box.draw_box(color=self.s.bg, bord_color=self.s.grey)
				self.boxes.add(box)

	def create_buttons(self):

		'''1. Creating keyboard buttons'''
		qwerty=['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
		for row in range(0,len(qwerty)):
			for letter_num in range(0,len(qwerty[row])):
				letter=qwerty[row][letter_num]

				button=Button(self)
				button_width,button_height=button.rect.size

				'''Calculating k - multiplier to arrange buttons evenly'''
				screen_width=self.screen.get_rect().width
				k=(screen_width/(len(qwerty[0])*button_width+(len(qwerty[0])+1)*4))
				button.rect.width=button_width*k

				'''Calculating border size on both sides'''
				border=(screen_width-len(qwerty[row])*button_width*k-
						(len(qwerty[row])-1)*4)/2

				button.x=k*(round(border)+(button_width+4)*letter_num)
				button.rect.x=button.x
				button.y=355+(button_height+4)*row
				button.rect.y=button.y
				button.draw_button(letter.upper())
				self.buttons.add(button)
		
		'''2. Creating ENTER and BACKSPACE buttons'''
		def _create_other_button(label):
			button=Button(self)
			button.rect.width=round(border)-4*2
			x=4 if label=='ENTER' else (screen_width-border+4)
			button.rect.x=x
			button.rect.y=355+(button_height+4)*2
			button.draw_button(label)
			self.buttons.add(button)
		_create_other_button('ENTER')
		_create_other_button('DEL')


if __name__=='__main__':
	words=open('words.txt').read().splitlines()
	word=random.choice(words)

	wordle=Wordle()
	wordle.run()