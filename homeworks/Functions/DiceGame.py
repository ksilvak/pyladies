import random

def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll
dice_roll()

player1 = 0
player2 = 0
player3 = 0
player4 = 0
player_one_rounds = 0
player_two_rounds = 0
player_three_rounds = 0
player_four_rounds = 0

while player1 != 6:
    player1 = dice_roll()
    player_one_rounds = player_one_rounds + 1
    print("Hráč 1: " + str(player1))

while player2 != 6:
    player2 = dice_roll()
    player_two_rounds = player_two_rounds + 1
    print("Hráč 2: " + str(player2))

while player3 != 6:
    player3 = dice_roll()
    player_three_rounds = player_three_rounds + 1
    print("Hráč 3: " + str(player3))

while player4 != 6:
    player4 = dice_roll()
    player_four_rounds = player_four_rounds + 1
    print("Hráč 4: " + str(player4))

print('Počet hodů: Hráč 1: ', player_one_rounds, ', Hráč 2: ', player_two_rounds, ', Hráč 3: ', player_three_rounds, ', Hráč 4: ', player_four_rounds)

if player_one_rounds > player_two_rounds and player_one_rounds > player_three_rounds and player_one_rounds > player_four_rounds:
    print('Vyhrál Hráč 1')
elif player_two_rounds > player_one_rounds and player_two_rounds > player_three_rounds and player_two_rounds > player_four_rounds:
    print('Vyhrál Hráč 2')
elif player_three_rounds > player_one_rounds and player_three_rounds > player_two_rounds and player_three_rounds > player_four_rounds:
    print('Vyhrál Hráč 3')
elif player_four_rounds > player_one_rounds and player_four_rounds > player_two_rounds and player_four_rounds > player_three_rounds:
   print('Vyhrál Hráč 4')
