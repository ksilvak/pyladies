from Move import move

def player_move(game_area):
	while True:
		position = int(input("Zadejte pozici umístění symbolu (0 - 19): "))

		if position < 0 or position > 19:
			print("Prosím zadejte číslo v rozmenzí 0 - 19.")
		elif game_area[position] != "-":
			print("Pole {} je obsazené, zkus to znovu.".format(position))
		else:
			return move(game_area, position, 'o')
