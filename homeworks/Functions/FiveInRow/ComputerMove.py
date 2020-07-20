import random
from Move import move

def computer_move(game_area):
	while True:
		position = random.randrange(0, 19)

		if game_area[position] == '-':
			return move(game_area, position, 'x')
