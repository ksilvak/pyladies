animals = {
    'Lilly': 'dog',
    'Barnabáš': 'rabbit',
    'Wingy': 'fish',
    'Lord': 'spider'
}

new_pair = dict(animals)
for k, v in new_pair.items():
    new = 'good ' + v
    new_pair['Wingy'] = 'cat'

    print('{} is {}'.format(k, new))

del new_pair['Lord']

print('#')

delete_pair = dict(new_pair)
for k, v in new_pair.items():
    new = 'good ' + v
    delete_pair['Wingy'] = 'cat'

    print('{} is {}'.format(k, new))
