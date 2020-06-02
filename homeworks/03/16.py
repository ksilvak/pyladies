number1 = int(input('První číslo: '))
number2 = int(input('Druhé číslo: '))
operation = input('Zadejte znaménko "+", "-", "*", "/": ')

if operation == '-': 
   print(number1, operation, number2, '=', number1 - number2)
elif operation == '+':
    print(number1, operation, number2, '=', number1 + number2)
elif operation == '*':
    print(number1, operation, number2, '=', number1 * number2)
elif operation == '/':
    print(number1, operation, number2, '=', number1 / number2)
else:
    print('Zadáváte špatný symbol, vyberte jeden z následujících "+", "-", "*", "/": ')



