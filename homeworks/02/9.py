from random import randrange

tah_pocitace = randrange(3)
kamen = tah_pocitace == 0
nuzky = tah_pocitace == 1
papir = tah_pocitace == 2

tah_cloveka = input('kámen, nůžky, nebo papír? ')

if tah_cloveka == 'kámen':
    if kamen:
        print('Plichta.')
    elif nuzky:
        print('Vyhrála jsi!')
    elif papir:
        print('Počítač vyhrál.')
elif tah_cloveka == 'nůžky':
    if kamen:
        print('Počítač vyhrál.')
    elif nuzky:
        print('Plichta.')
    elif papir:
        print('Vyhrála jsi!')
elif tah_cloveka == 'papír':
    if kamen:
        print('Vyhrála jsi!')
    elif nuzky:
        print('Počítač vyhrál.')
    elif papir:
        print('Plichta.')
else:
    print('Nerozumím.')
