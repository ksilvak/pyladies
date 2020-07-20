from PlayerMove import player_move
from ComputerMove import computer_move
from Evaluate import evaluate


def game1d():
	game_area = "-" * 20
	round_count = 0

	while True:
		round_count = round_count + 1
		print(game_area)
		game_area = player_move(game_area)

		if evaluate(game_area) != '-':
			break

		game_area = computer_move(game_area)

		if evaluate(game_area) != '-':
			break

	print('Kolo',round_count, game_area)

	if evaluate(game_area) == '!':
		print('Remíza')
	elif evaluate(game_area) == 'o':
		print('Vhrál jsi!')
	elif evaluate(game_area) == 'x':
		print('Vyhrál počítač')

game1d()
