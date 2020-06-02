string = input('Zadej původní řetězec: ')
position = int(input('Na jaké pozici bude výměna? '))
x = input('Jaký x tam bude? ')

print('Po výměně je takovýto výsledek:')

print(string[:position] + x + string[position + 1:])


firstName = input('Zadejte jmeno:')
secondName = input('Zadejte příjmnení:')

print(firstName[0].upper(), secondName[0].upper())
