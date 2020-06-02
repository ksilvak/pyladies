print('Odpovídej "ano" nebo "ne".')
happy_string = input('Jsi šťastná? ')
if happy_string == 'ano':
    happy = True
elif happy_string == 'ne':
    happy = False
else:
    print('Nerozumím!')


rich_string = input('Jsi bohatá? ')
if rich_string == 'ano':
    rich = True
elif rich_string == 'ne':
    rich = False
else:
    print('Nerozumím!')

if happy:
    print('Zkus míň utrácet.')
    if rich:
        print('Gratuluji!')
elif rich:
    print('Zkus se víc usmívat.')
else:
    print('To je mi líto.')
