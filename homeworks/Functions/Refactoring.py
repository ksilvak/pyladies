import numbers

# Correct format - 6 numbers, / and 4 numbers
personal_id = input('Zadejte Vaše rodné číslo: ')

def is_format_ok(personal_id):
    if personal_id[0:6].isdigit() & personal_id[7:11].isdigit():
        if personal_id[6] == '/':
            return True
        else:
            return False
    else:
        return False

print(is_format_ok(personal_id))

# Is divisible by eleven

personal_id = input('Zadejte Vaše rodné číslo: ')

def is_divisible(personal_id, n):
    number = int(personal_id[0:6] + personal_id[7:11])
    if number % n == 0:
        return True
    else:
        return False 
print(is_divisible(personal_id, 11))

# Gender
personal_id = input('Zadejte Vaše rodné číslo: ')

def gender(personal_id):
    if int(personal_id[2:4]) - 50 > 0:
        return 'Žena'
    else:
        return 'Muž'
print(gender(personal_id))

# Birthday
personal_id = input('Zadejte Vaše rodné číslo: ')

def birth_day(personal_id):
    day = personal_id[4:6]
    month = personal_id[2:4]
    year = personal_id[0:2]
    
    if int(personal_id[2:4]) - 50 > 0:
        month = int(personal_id[2:4]) - 50
        birth = [day, month, year]
        return birth
    else:
        birth = [day, month, year]
        return birth
print(birth_day(personal_id))
