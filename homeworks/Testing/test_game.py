import pytest
from FiveInRow import evaluate, move, player_move, game1d
from ai import computer_move

def test_evaluate_win_x():
	assert evaluate("xxx-----------------") == "x"
	assert evaluate("--------xxx---------") == "x"
	assert evaluate("-----------------xxx") == "x"
	assert evaluate("-xoxoxxxoxoxoxoxoxox") == "x"
	assert evaluate("-xooxxooxxooxxoxxxoo") == "x"
	assert evaluate("xxxoxoxoxoxoxoxoxox-") == "x"
	assert evaluate("oxxxoxoxxooxxooxxoo-") == "x"
	assert evaluate("oxoxoxoxo-oxoxoxoxxx") == "x"
	assert evaluate("xxooxxoox-ooxxooxxxo") == "x"

def test_evaluate_win_o():
	assert evaluate("ooo-----------------") == "o"
	assert evaluate("--------ooo---------") == "o"
	assert evaluate("-----------------ooo") == "o"
	assert evaluate("-xoxoxoxoooxoxoxoxox") == "o"
	assert evaluate("-xoooxooxxooxxooxxoo") == "o"
	assert evaluate("xoooxoxoxoxoxoxoxox-") == "o"
	assert evaluate("oooxxooxxooxxooxxoo-") == "o"
	assert evaluate("oxoxoxoxo-oxoxoxooox") == "o"
	assert evaluate("xxooxxoox-ooxxooxooo") == "o"

def test_evaluate_draw():
	assert evaluate("oxoxoxoxoxoxoxoxoxox") == "!"
	assert evaluate("xxooxxooxxooxxooxxoo") == "!"

def test_game_run():
	assert evaluate("--------------------") == "-"
	assert evaluate("xx----------------oo") == "-"
	assert evaluate("-xoxoxoxoxoxoxoxoxox") == "-"
	assert evaluate("-xooxxooxxooxxooxxoo") == "-"
	assert evaluate("xoxoxoxoxoxoxoxoxox-") == "-"
	assert evaluate("xooxxooxxooxxooxxoo-") == "-"
	assert evaluate("oxoxoxoxo-oxoxoxoxox") == "-"
	assert evaluate("xxooxxoox-ooxxooxxoo") == "-"

def test_move_x():
	assert move("--------------------", 0, "x") == "x-------------------"
	assert move("--------------------", 10, "x") == "----------x---------"
	assert move("--------------------", 19, "x") == "-------------------x"

def test_move_o():
	assert move("--------------------", 0, "o") == "o-------------------"
	assert move("--------------------", 10, "o") == "----------o---------"
	assert move("--------------------", 19, "o") == "-------------------o"

def test_computer_move_middle():
	game_area = "xxxooxxooo-xxoxooxox"
	result = computer_move(game_area)
	assert len(result) == 20
	assert result.count("x") == 11
	assert result.count("o") == 9


def test_computer_move_start():
	game_area = "-xoxoxoxoxoxoxoxoxox"
	result = computer_move(game_area)
	assert len(result) == 20
	assert result.count("x") == 11
	assert result.count("o") == 9

def test_computer_move_end2():
	game_area = "xoxoxoxoxoxoxoxoxo--"
	result = computer_move(game_area)
	assert len(result) == 20
	assert result.count("x") == 10
	assert result.count("o") == 9
	assert result.count("-") == 1


if __name__ == "__main__":
    pytest.main()
