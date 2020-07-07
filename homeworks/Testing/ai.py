import random

def computer_move(game_area):
	while True:
		position = random.randrange(0, 19)

		if game_area[position] == '-':
			return game_area[:position] + 'x' + game_area[position + 1:]
