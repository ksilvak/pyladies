fish = float(input('Zadej váhu ryby: '))

if fish > 1 and fish < 5:
	print('lepší než nic')
elif fish > 5 and fish < 11:
	if fish == 9 or fish == 10:
		print('Dobrý průměr')
	else:
		print('To vypadá dobře')
elif fish > 10:
	print('Dnes se konečně nažereme')
else:
	print('Asi chyba v matrixu')
