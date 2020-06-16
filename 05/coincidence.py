import random

## shufle()

deck = []

for color in 'spade' , 'heart', 'diamonds', 'cross':
    for value in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
        deck.append(str(value) + color)
print(deck)

random.shuffle(deck)
print(deck)

## choice()

options = ['kámen', 'nůžky', 'papír']
computer = random.choice(options)
print(computer)