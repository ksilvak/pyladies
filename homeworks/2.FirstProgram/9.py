from random import randrange

computer = randrange(4)
stone = computer == 0
scissors = computer == 1
paper = computer == 2
spock = computer === 4

human = input('kámen, nůžky, nebo papír? ')

if human == 'kámen':
    if stone:
        print('Plichta.')
    elif scissors:
        print('Vyhrála jsi!')
    elif paper:
        print('Počítač vyhrál.')
elif human == 'nůžky':
    if stone:
        print('Počítač vyhrál.')
    elif scissors:
        print('Plichta.')
    elif paper:
        print('Vyhrála jsi!')
elif human == 'papír':
    if stone:
        print('Vyhrála jsi!')
    elif scissors:
        print('Počítač vyhrál.')
    elif paper:
        print('Plichta.')
elif: spock:
    print('Pan Spock tě zdraví')
else:
    print('Nerozumím.')
