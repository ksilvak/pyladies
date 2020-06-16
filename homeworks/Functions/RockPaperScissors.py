from random import randrange

computer = randrange(4)
stone = computer == 0
scissors = computer == 1
paper = computer == 2
human = False

while human == False:
    human = input('kámen, nůžky, nebo papír? ')
    if human == 'kámen' and stone or human == 'nůžky' and scissors or human == 'papír' and paper:
        print('Plichta.')
    elif human == 'kámen' and scissors or human == 'nůžky' and paper or human == 'papír' and stone:
        print('Vyhrála jsi!')
    elif human == 'kámen' and paper or human == 'nůžky' and stone or human == 'papír' and scissors:
        print('Počítač vyhrál.')
    elif human == 'spock':
        print('Pan Spock tě zdraví')
    elif human == 'konec':
        print('Děkuji za hru')
        break
    else:
        print('Nerozumím.')
    human = False
