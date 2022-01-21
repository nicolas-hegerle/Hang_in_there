import re, os, nltk, random, string
from nltk.corpus import words
from draw_hangman import draw_mistakes


pattern = '[A-z]'
tries = 10
alphabet = [i for i in string.ascii_lowercase]


def hide_word():

	global secret_word
	global hidden_word

	hidden_word = []

	secret_word = list(secret_word)
	if len(secret_word) != 0:
		for i in secret_word:
			if re.match(pattern, i) != None:
				hidden_word.append('_')
			else:
				hidden_word.append(i)
	hidden_word[0] = secret_word[0]
	hidden_word[-1] = secret_word[-1]
	print('\nHere is the hidden word you need to find: ')
	print(''.join(hidden_word))

	return hidden_word

def letter_test():

	global tries
	global hidden_word
	global secret_word
	found_letters = []
	tried_letters = []

	while hidden_word != secret_word and tries > 0 :

		try_letter = input('\nWhat letter do you think is in the secret word? ').lower()

		try:
			assert (len(try_letter)) == 1
			assert try_letter in alphabet

			if try_letter in tried_letters:
				print('\nYou already tried this letter, please enter another letter')

			elif try_letter in found_letters:
				print('\nYou already found this letter, please enter another letter')

			elif try_letter	not in secret_word:
				tries -= 1
				if tries != 0:
					print()
					draw_mistakes(tries)
					print('\nThis letter is not in the word. You have ', tries, ' tries left\n')
					tried_letters.append(try_letter)
				else:
					print()
					draw_mistakes(tries)
					print()

			else:
				for i in range(1 , len(secret_word) - 1):
					if try_letter == secret_word[i]:
						hidden_word.pop(i)
						hidden_word.insert(i , try_letter)
				found_letters.append(try_letter)


			print('Here is the current status of the hidden word : ' + ''.join(hidden_word))
			print('Here are the letters you already found: ' + ','.join(found_letters))
			print('Here are the letters you already tried: ' + ','.join(tried_letters))
		
		except AssertionError:
			print("!!Please enter a single lower case letter!!")
		
		if tries == 0:
			print("\nSorry you exhausted all your chances. \nThe word you were supposed to find was : ", ''.join(secret_word))
			input("Press Enter to continue")
		if hidden_word == secret_word:
			print("\nCongratulations you found the hidden word!!")
			input("Press Enter to continue")
		

print("\n----FIND THE SECRET WORD----\n")
draw_mistakes(10)

choice = ""

while choice not in ['4', 'q', 'Q', 'Quit', 'QUIT'] :

	print("""\nWhat would you like to do?
1. You have no friends but you want to play alone. Select 1
2. You are lucky to have friends, play against one-another. Select 2
3. You do not know how to play and want to read the rules. Select 3
4. Actually you do not want to play, you can quit the game. Select 4 or Q
		""")

	choice = input("\nPlease enter your choice: ")

	if choice == '1':
		secret_word = ''
		word_list = words.words()
		while len(secret_word) <= 7:
			secret_word = word_list[random.randint(0, len(word_list))]
		hide_word()
		letter_test()
		choice = ""

	elif choice == '2':
		secret_word = ''
		while len(secret_word) == 0 :
			secret_word = input('Please enter your secret word? ')
			os.system('clear')
		hide_word()
		letter_test()
		choice = ""

	elif choice == '3':
		print("""\nThe purpose of the game is to find the secret word.
You have {} chances to find all the letters of the secret word.
Letters you have already found will appear if they are in the hidden word.
If the letter you enter is not in the word you loose a point.
When you exhausted your chances you loose and the word is revealed.
Good luck!.\n""".format(tries))
		choice = ""
		continue

	elif choice not in ['1', '2', '3', '4', 'q', 'Q', 'Quit', 'QUIT']:
		print("\nI did not get what your choice was: ")
		continue
