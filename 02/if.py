stastna = input('Jsi šťastná?')
bohata = input('Jsi bohatá?')

if stastna == 'ano':

	if bohata == 'ano':
		print('Gratulujeme')
	else:
		print('Neutrácej tak')
else:
	if bohata == 'ano':
		print('Usměj se')
	else:
		print('To je mi líto')
