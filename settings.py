class Settings():

	def __init__(self):
		'''Window settings'''
		self.screen_width=215
		self.screen_height=455

		'''Colors'''
		self.text_color=(250,250,250)
		self.bg=(17,17,19)
		self.green=(82,140,79)
		self.yellow=(181,157,57)
		self.grey=(58,58,60)
		self.not_used=(130,131,133)

		'''Messages'''
		self.messages = {}
		mottos = ['Genius', 'Magnificent', 'Impressive', 'Splendid', 'Great', 'Phew']
		for i in range(1,7):
			self.messages[i] = mottos[i-1]

		'''Timer'''
		self.timer_length=1000

		'''Fonts'''
		self.logo_font='stymie/STYMIEXB.ttf'
		self.logo_size=18
		self.text_font='Helvetica Neue'
		self.text_size=20
		self.box_font_size=25
		self.button_font_size=11

		'''Sizes'''
		self.box_size=31
		self.button_width=17
		self.button_height=29

		'''Alphas'''
		self.full=225
		self.transparent=127