def evaluate(game_area):
	if "xxx" in game_area:
		return "x"
	elif "ooo" in game_area:
		return "o"
	elif "-" not in game_area:
		return "!"
	else:
		return "-"
