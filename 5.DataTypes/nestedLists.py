nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(nested_list[0])
print(nested_list[1][0])


size = 11
multiplication = []
for a in range(size):
    row = []
    for b in range(size):
        row.append(a * b)
    multiplication.append(row)

print(multiplication[2][3])
print(multiplication[5][2])
print(multiplication[8][7])

for row in multiplication:
    for number in row:
        print(number, end=' ')
    print()
