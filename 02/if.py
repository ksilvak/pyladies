happy = input('Jsi šťastná?')
rich = input('Jsi bohatá?')

if happy == 'ano':

	if rich == 'ano':
		print('Gratulujeme')
	else:
		print('Neutrácej tak')
else:
	if rich == 'ano':
		print('Usměj se')
	else:
		print('To je mi líto')
