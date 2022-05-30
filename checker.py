def check_wordle(word, guess):
	'''Функция ищет все возможные комбинации выдачи результата попытки
	Комбинации возникают из-за возможности по разному показить желтые буквы, если их несколько'''
	check=['*']*len(guess)
	word=list(word)
	guess=list(guess)

	#Зеленые буквы - на своих местах. Затем убираем их из списков слова и попытки
	for _ in range(0, 5):
		if word[_] == guess[_]:
			check[_] = 'G'
			word[_] = '*' #разные символы для пустых значений, чтобы не совпали
			guess[_] = ''

	#Желтые буквы ищем в несколько этапов:
	# 1) находим все альтернативы для каждой буквы 
	for _ in range(0, 5):
		if guess[_] in word:
			check[_]=f"alt_{guess[_]}"

	check_full=[]
	args=[]
	
	# 2) для альтернатив формируем список args со всеми возможными комбинациями
	#    в зависимости от количества букв в попытке и в загаданном слове
	import itertools
	for alt in set([val for val in check if val.startswith('alt')]):
		letter = alt[-1] #сама буква
		count = word.count(letter) #количество таких букв в загаданном слове
		index_pos = [i for i in range(len(check)) if check[i]==alt] #позиции в guess
		if count>=len(index_pos): #если элементов меньше позиций, то берем эти элементы
			args.append(list(itertools.combinations(index_pos, len(index_pos))))
		else: #в других случаях считаем комбинации позиций и количества буквы в слове
			args.append(list(itertools.combinations(index_pos, count))) #комбинации
		
	# 3) в слове может быть несколько комбинаций комбинаций, если альтернатива не одна
	#    тогда ищем все сочетания комбинаций позиций, заполняем их Y, а остальные - W
	for combo in itertools.product(*args): #произведение множеств
		new_check=check.copy()
		for index in sum(combo, ()):
			new_check[index]='Y'
		new_check = ['W' if (x!='Y' and x!='G') else x for x in new_check]
		check_full.append(new_check)
	
	return check_full #убираем дубликаты