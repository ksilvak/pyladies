computer = 'kámen'
human = input('kámen, nůžky, nebo papír? ')

if human == 'kámen' and computer == 'kámen' or human == 'nůžky' and computer == 'nůžky' or human == 'papír' and computer == 'papír':
    print('Plichta.')
elif human == 'kámen' and computer == 'nůžky' or human == 'nůžky' and computer == 'papír' or human == 'papír' and computer == 'kámen':
    print('Vyhrála jsi!')
elif human == 'kámen' and computer == 'papír' or human == 'nůžky' and computer == 'kámen' or human == 'papír' and computer == 'nůžky':
    print('Počítač vyhrál.')
else:
    print('Nerozumím.')
