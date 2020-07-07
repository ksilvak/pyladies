from ai import computer_move


def evaluate(game_area):
	if "xxx" in game_area:
		return "x"
	elif "ooo" in game_area:
		return "o"
	elif "-" not in game_area:
		return "!"
	else:
		return "-"


def move(game_area, position, symbol):
	return game_area[:position] + symbol + game_area[position + 1:]


def player_move(game_area):
	while True:
		position = int(input("Zadejte pozici umístění symbolu (0 - 19): "))

		if position < 0 or position > 19:
			print("Prosím zadejte číslo v rozmenzí 0 - 19.")
		elif game_area[position] != "-":
			print("Pole {} je obsazené, zkus to znovu.".format(position))
		else:
			return move(game_area, position, 'o')

def game1d():
	game_area = ""
	while True:
		print(game_area)

		if evaluate(game_area) == '-':
			game_area = player_move(game_area)
			game_area = computer_move(game_area)
			continue
		elif evaluate(game_area) == '!':
			print('Remíza')
			break
		elif evaluate(game_area) == 'o':
			print('Vhrál jsi!')
			break
		elif evaluate(game_area) == 'x':
			print('Vyhrál počítač')
			break
