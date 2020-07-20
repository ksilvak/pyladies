def yes_or_no(question):
    while True:
        odpoved = input(question)
        if odpoved[0] == 'a' or odpoved[0] == 'A':
            return True
        elif odpoved[0] == 'n' or odpoved[0] == 'N':
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne".')

if yes_or_no('Chceš si zahrát hru? '):
    print('OK! Ale napřed si ji musíš naprogramovat.')
else:
    print('Škoda.')
    