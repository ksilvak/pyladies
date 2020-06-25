def move(game_area, position, symbol):
	return game_area[:position] + symbol + game_area[position + 1:]
