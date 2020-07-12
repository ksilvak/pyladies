mountains = {
    'Mount Everest': '8,9',
    'K2': '8,6',
    'Kangchenjunga': '8,58',
    'Lhotse': '8,51',
    'Makalu': '8,48',
}

for k in mountains.keys():
    print(k)

print(' ')

for k in mountains.values():
    print(k)

print(' ')

for k, value in mountains.items():
     print('{} is {} metres tall'.format(k, value))
     