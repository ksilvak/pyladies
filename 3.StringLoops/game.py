from random import randrange


result = 0

while result < 21:
    print('Máš', result, 'bodů')
    answer = input('Otočit kartu?')

    if answer == 'ano':
       karta = randrange(2,11)
       print('Otočila jsi:', karta)
       result = result + karta

    elif answer == 'ne':
        break
    else:
        print('Nerozumím! Odpovídej "ano", nebo "ne"')

if result == 21:
    print('gratuluji k výhře')
elif result > 21:
     print('Smůla!', result, 'bodů je moc!')
else:
    print('Chybělo jen', 21 - result, 'bodů!')
