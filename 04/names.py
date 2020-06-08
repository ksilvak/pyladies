records =  ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

incorrect_records = []
correct_records = []
corrected_records = []

for i in records:
    full_name = i.split(' ')
    first_name = full_name[0]
    second_name = full_name[1]
    if first_name[0].islower() or second_name[0].islower():
        incorrect_records.append(i) 
    elif not first_name[0].islower() and not second_name[0].islower():
        correct_records.append(i)

    corrected_records.append(first_name.capitalize() + ' ' + second_name.capitalize())
print(incorrect_records)
print(correct_records)
print(corrected_records)
