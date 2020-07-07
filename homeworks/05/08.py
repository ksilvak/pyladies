import numbers

personal_id = input('Zadejte Vaše rodné číslo: ')

if personal_id[0:6].isdigit() & personal_id[7:11].isdigit():
    if personal_id[6] == '/':
        print('Formát je ok')
    else: 
        print('Špatný formát rodného čísla')
else:
   print('Špatný formát rodného čísla')
