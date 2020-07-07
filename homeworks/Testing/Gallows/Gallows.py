import random
import img


words = random.choice(['duha', 'lavina', 'koniklec'])
unsuccessful = []
used_letters = []

def move(area):
	letter = input('Hádej písmeno: ')
	if letter.isdigit() or letter == "" or letter.isspace():
		print('Zadej pouze písmeno')
	elif len(letter) > 1:
		print('Zadávej po jednom')
	elif letter not in words:
		print('Bohužel, zkus jiné písmeno')
		used_letters.append(letter)
		unsuccessful.append(len(unsuccessful))
		img.pictures[unsuccessful[-1]]()
	elif letter in used_letters:
		print('Bohužel, zkus jiné písmeno')
	elif letter in words and letter not in used_letters:
		used_letters.append(letter)
		print('Ano, je tam!')

		return(area[:words.index(letter)] + letter + area[words.index(letter): + 1])

def game():
	area = len(words) * '_'
	print(area)
	while True:
		if "_" in area:
			area = move(area)
			print(area)
		elif len(unsuccessful) > 8:
			print('Prohrál jsi')
			break
		else:
			return 'Vyhrál jsi'

game()
