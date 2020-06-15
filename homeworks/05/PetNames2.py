animals = {
    'Lilly': 'dog',
    'Barnabáš': 'rabbit',
    'Wingy': 'fish',
    'Lord': 'spider'
}

new_pair = dict(animals)
for k in new_pair:
    new_pair['Wingy'] = 'good cat'
    new_pair[k] = 'good ' + new_pair[k]

print(new_pair)

del new_pair['Lord']

print(new_pair)
