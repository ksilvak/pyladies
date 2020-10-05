import img


def move(pole, words, attempts, used_letters):
	letter = input("Hádej písmeno: ")
	if letter.isdigit() or letter not in words or (letter in words and len(letter)!=1):
		if letter.isdigit() or letter == "" or letter.isspace():
			print("Zadej písmeno!")
		elif len(letter)!=1:
			print("Zadává se jen po jednom písmenu")
		elif letter in used_letters:
			print("Opakuješ se, toto písmeno tam vážně není")
		else:
			used_letters.append(letter)
			print("Toto písmeno tu není")
		attempts.append(len(attempts))
		img.pictures[attempts[-1]]()
		return pole
	else:
		print("Jooo")
		return pole[:words.index(letter)] + letter + pole[words.index(letter) + 1:]
