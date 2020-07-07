import numbers

personal_id = input('Zadejte Vaše rodné číslo: ')

if personal_id[0:6].isdigit() & personal_id[7:11].isdigit():
    if personal_id[6] == '/':
        print(True)
    else:
        print(False)
else:
    print(False)
if int(personal_id[2:4]) - 50 > 0 and int(personal_id[2:4]) - 50 > 12:
   (print('Špatně zadané rodné číslo, nelze vypočítat'))
elif int(personal_id[2:4]) - 50 > 0:
    print('Žena')
elif int(personal_id[2:4]) > 12:
    (print('Špatně zadané rodné číslo, nelze vypočítat'))
else:
    print('Muž')


day = personal_id[4:6]
month = personal_id[2:4]
year = personal_id[0:2]

if int(personal_id[2:4]) - 50 > 0 and int(personal_id[2:4]) -50 < 13:
    month = int(personal_id[2:4]) - 50
    print('Datum narození: ', day,'.', month,'.',year)
elif int(personal_id[2:4]) - 50 > 0 :
	(print('Špatně zadané rodné číslo, nelze vypočítat'))
elif int(personal_id[2:4]) > 12:
	(print('Špatně zadané rodné číslo, nelze vypočítat'))
else:
    print('Datum narození: ', day,'.', month,'.',year)

# Is divisible by eleven

def is_divisible(personal_id, n):
    number = int(personal_id[0:6] + personal_id[7:11])
    if number % n == 0:
        return True
    else:
        return False
print(is_divisible(personal_id, 11))
