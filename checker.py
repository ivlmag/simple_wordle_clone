def check_wordle(word, guess):
	'''Finding all the combinations to present result
	There can be more than one way to show result due to the fact, 
	that there can be more than one yellow letter in the word'''
	check=['*']*len(guess)
	word=list(word)
	guess=list(guess)

	'''Green letters are in the right position. 
	Extract them from all lists, so they won't affect the result anymore'''
	for _ in range(0, 5):
		if word[_] == guess[_]:
			check[_] = 'G'
			'''Different symbols for empty elements in different lists,
			so the won't overlap'''
			word[_] = '*'  
			guess[_] = ''

	#We will find yellow letters in two steps:
	# 1) mark all the alternative positions for each yellow letter 
	for _ in range(0, 5):
		if guess[_] in word:
			check[_]=f"alt_{guess[_]}"

	check_full=[]
	args=[]
	
	# 2) for every alternative letter we costruct args list with 
	#    all possible combinations depending on number of letter in guessed word
	#    and input word
	import itertools
	for alt in set([val for val in check if val.startswith('alt')]):
		letter = alt[-1] #the letter itself
		count = word.count(letter) #number of letter in the guessed word
		index_pos = [i for i in range(len(check)) if check[i]==alt] #position in input
		if count>=len(index_pos): #if number of letter is less than positions, take the positions indexes
			args.append(list(itertools.combinations(index_pos, len(index_pos))))
		else: #else we calculate the combinations between number of letter and indexes in input
			args.append(list(itertools.combinations(index_pos, count))) 
		
	# 3) there can be several combinations in the guess, 
	#    therefore we need to calculate combinations of combinations
	for combo in itertools.product(*args): #Cartesian product of combinations
		new_check=check.copy()
		for index in sum(combo, ()):
			new_check[index]='Y'
		new_check = ['W' if (x!='Y' and x!='G') else x for x in new_check]
		check_full.append(new_check)
	
	return check_full 