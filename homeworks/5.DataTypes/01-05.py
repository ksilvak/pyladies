animals = ['pes', 'kocka', 'kralik', 'had']

for k in animals: 
    if len(k) < 5:
        print(k)

print(' ')

for k in animals: 
    if k[0] == 'k':
        print(k)
   
print(' ')


value = input('Zadejte hledané slovo: ')

for k in animals: 
    print(value in k)

print(' ')

animals1 = ['pes', 'kocka']
animals2 = ['kralik', 'had']
animals1.extend(animals2)

print(animals1)

animals1.remove(animals1[3])
animals1.remove(animals1[2])
print(animals1)

animals1.extend(animals2)
animals1.remove(animals1[0])
animals1.remove(animals1[0])
print(animals1)

print(' ')

animals.sort()
print(animals)
