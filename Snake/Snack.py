import random


# Svačina pro hada

def randomSnack(rows, item):
	positions = item.body

	while True:
		x = random.randrange(rows)
		y = random.randrange(rows)
		if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:  # pro ujištění, že nedám svačinu na pozici hada
			continue # pokud by měla být kostička na stejné pozici, jako je had, tak pokračovat znovu
		else:
			break
	return(x, y)
