from move import move
import random


words = random.choice(["deka", "lano", "lepricon"])
attempts = []
used_letters = []

def game():
	pole = len(words)*"_"
	print(pole)
	while True:
		if len(attempts) > 8:
			print("Konec hry")
			break
		elif "_" in pole:
			pole = move(pole, words, attempts, used_letters)
			print(pole)
		else:
			print("Výhra")
			print("Tvoje slovo bylo: {}".format(words))
			break
