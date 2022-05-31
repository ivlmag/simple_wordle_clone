import random
from colorama import init, Fore, Back, Style
from checker import check_wordle


def text_edit(guess, result, alphabet):
	editted_text = []

	def _letter_paint(letter, color):
		letter_painted = ''
		if color=='Green':
			letter_painted = Back.GREEN + letter.upper() 
		elif color=='Yellow':
			letter_painted = Back.YELLOW + letter.upper() 
		elif color=='Grey':
			letter_painted = Back.WHITE + Fore.BLACK + letter.upper()
		else:
			letter_painted = letter.upper()

		return letter_painted + Style.RESET_ALL

	def _alphabet_edit():
		for i in range(0, len(alphabet)):
			letter = alphabet[i]
			alphabet_print[i] = _letter_paint(letter, alphabet_dict[letter])

	for _ in range(0, len(result)):
		if result[_]=='G':
			color = 'Green'
			alphabet_dict[guess[_].upper()] = color
			editted_text.append(_letter_paint(guess[_], color))
		if result[_]=='Y':
			color = 'Yellow'
			if alphabet_dict[guess[_].upper()] != "Green":
				alphabet_dict[guess[_].upper()] = color
			editted_text.append(_letter_paint(guess[_], color))
		if result[_]=='W':
			color = 'Grey'
			if (alphabet_dict[guess[_].upper()] != "Green" or
				alphabet_dict[guess[_].upper()] != "Yellow"):
				alphabet_dict[guess[_].upper()] = color
			editted_text.append(_letter_paint(guess[_], color))

		alphabet_print = alphabet.copy()
		_alphabet_edit()

	if result==['G']*5:
		joined_text = ''.join(editted_text)+'\n'
	else:
		joined_text = ''.join(editted_text)+'\n'+'-'*20+'\n'+' '.join(alphabet_print)+'\n'

	return joined_text

def main(alphabet):
	words = open('words.txt').read().splitlines()

	word_to_guess = random.choice(words)

	attempt = 0

	for letter in range(0, len(alphabet)):
		alphabet_dict[alphabet[letter].upper()] = "Not Used"

	while True:
		if attempt==6:
			print(f'The word was "{word_to_guess}".')
			break
		guess = input('Enter five-letter word (print "q" to exit): ')
		if guess=='q':
			break
		else:
			if (guess not in words) or len(guess)!=5:
				print("Can't use this word")
			else:
				attempt+=1
				result = random.choice(check_wordle(word_to_guess, guess))
				print(text_edit(guess, result, alphabet))
				if result==['G']*5:
					print('Congratulations!')
					break

if __name__ == '__main__':
	init()
	import string
	alphabet = list(string.ascii_uppercase)
	alphabet_dict={}
	main(alphabet)