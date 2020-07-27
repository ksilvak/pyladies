file_ = open('poem.txt', encoding='utf-8')
content = file_.read()
file_.close()

print(content)


print('Slyšela jsem tuto básničku: ')
print()

with  open('poem.txt', encoding='utf-8') as file_:
	for line in file_:
		line = line.rstrip()
		print('	' + line)

print()
print('Líbí se ti ?')

with  open('second-poem.txt', mode='w', encoding='utf-8') as file_:
	print('Naše staré hodiny', file=file_)
	print('Bijí', 2+2, 'hodiny', file=file_)


with  open('second-poem.txt', encoding='utf-8') as file_:
	content = file_.read()
	print(content)
