string = input('Zadej původní řetězec: ')
pozice = int(input('Na jaké pozici bude výměna? '))
znak = input('Jaký znak tam bude? ')

print('Po výměně je takovýto výsledek:')

print(string[:pozice] + znak + string[pozice + 1:])


jmeno = input('Zadejte jmeno:')
prijmeni = input('Zadejte příjmnení:')

print(jmeno[0].upper(), prijmeni[0].upper())

