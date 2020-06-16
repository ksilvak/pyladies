from math import pi

def obsah_elipsy(a,b):
	return pi*a*b

obsah_elipsy(7, 8)

def objem(a, b, height):
	return obsah_elipsy(a, b)*height

print(objem(3,5,2))
