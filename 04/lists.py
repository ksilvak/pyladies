import random

## lists

prime_numbers = [2, 3, 5, 7, 11, 13, 17]
print(prime_numbers)
prime_numbers.append(19)
print(prime_numbers)

## append() přidá daný prvek

a = [1, 2, 3]
b = a
print(b)
a.append(4)
print(b)

## extendes() přidá více prvků

numbers = [23, 29, 31]
numbers.extend(numbers)
print(numbers)

## extends with range()

lists = []
lists.extend('abcdef')
lists.extend(range(10))
print(lists)

## change elements

number = [1, 0, 3, 4]
number[1] = 2
print(number)

## manual delete

number = [1, 2, 3, 4]
number[1:-1] = [0, 0, 0, 0, 0, 0]
print(number)
number[1:-1] = []
print(number)

## command del

numbers = [1, 2, 3, 4, 5, 6]
del numbers[-1]
print(numbers)
del numbers[3:5]
print(numbers)

## pop() - odtsraní a vrátí poslední prvek v seznamu
## remove() - najde prvek a odstraní ho
## clear() - vyprázdní celý list

numbers = [1, 2, 3, 'abc', 4, 5, 6, 12]
last = numbers.pop()
print(last)

numbers.remove(numbers[3])  ## numbers.remove('abc')
print(numbers)

numbers.clear()
print(numbers)

## sort() reverse=True - seřadí v opačném pořadí

lists = [4, 7, 8, 3, 5, 2, 4, 8, 5]
lists.sort()
print(lists)

lists.sort(reverse=True)
print(lists)

## operation
song = ['C', 'E', 'G'] * 2 + ['E', 'E', 'D', 'E', 'F', 'D'] * 2 + ['E', 'D', 'C']
print(song)

## len() count() index() in

song = ['C', 'E', 'G'] * 2 + ['E', 'E', 'D', 'E', 'F', 'D'] * 2 + ['E', 'D', 'C']
print(len(song))
print(song.count('D'))
print(song.index('D'))
print('D' in song)

## condition
list1 = []
if list1:
    print('V seznamu něco je!')
else:
    print('Seznam je prázdný!')

## list()
##int() převede na celé číslo, str() na string

alphabet = list('abcdefghijklmnopqrstuvwxyz')
number = list(range(10))
print(alphabet)
print(number)

## Tvoření listu
## list() udělá z listu list :)  => vytvoří nový list, ten má stejné prvky, jako původní, ale mění se nezávisle na tom původním

a = [1, 2, 3]
b = list(a)

print(b)
a.append(4)
print(b) ## b zůstane [1, 2, 3]

    ## prázný list a pak ho naplnit pomocí append

power_two = []
for number in range(10):
    power_two.append(2 ** number)
print(power_two)

deck = []
for color in 'spade' , 'heart', 'diamonds', 'cross':
    for value in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
        deck.append(str(value) + color)
print(deck)

## split() join()

words = 'Tato věta je složitá, rozdělme ji na slova!'.split()
print(words)

example = '3A,8B,2E,9D'.split(',')
print(example)

sentence = ' '.join(words)
print(sentence)
