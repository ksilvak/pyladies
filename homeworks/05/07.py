import numbers

personal_id = input('Zadejte Vaše rodné číslo: ')

if personal_id[0:6].isdigit() & personal_id[7:11].isdigit():
    if personal_id[6] == '/':
        print(True)
    else: 
        print(False)
else:
    print(False)

if int(personal_id[2:4]) - 50 > 0:
    print('Žena')
else: 
    print('Muž')


day = personal_id[4:6]
month = personal_id[2:4]
year = personal_id[0:2]

if int(personal_id[2:4]) - 50 > 0:
    month = int(personal_id[2:4]) - 50
    print('Datum narození: ', day,'.', month,'.',year)
else:
    print('Datum narození: ', day,'.', month,'.',year)

