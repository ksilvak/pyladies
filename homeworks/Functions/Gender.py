import numbers

second_name = input('Zadejte Vaše příjmení číslo: ')

if second_name[-3:] == 'ová':
    print('Jsi žena')
else: 
    print('Jsi muž')
