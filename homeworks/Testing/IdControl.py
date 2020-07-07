personal_id = input('Zadej číslo: ')

try:
	int(personal_id[0:6])
	int(personal_id[7:11])
	if personal_id[6] != '/' or len(personal_id) > 11:
		raise ValueError
	print('Rodné číslo je ok')
except (ValueError, IndexError):
	print('Špatný formát')
