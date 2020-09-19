from Cube import cube
from MessageBox import message_box
from Snack import randomSnack
from Snake import snake
import pygame


def redrawWindow(surface):
	global rows, width, s, snack
	surface.fill((0, 0, 0))
	s.draw(surface)
	snack.draw(surface)
	pygame.display.update()

def main():
	global width, rows, s, snack
	width = 500
	rows = 20
	win = pygame.display.set_mode((width, width))
	s = snake((194, 14, 95), (10, 10))
	snack = cube(randomSnack(rows, s), color=(255, 255, 255))
	flag = True

	clock = pygame.time.Clock()

	while flag:
	# rychlost hada
		pygame.time.delay(50)
		clock.tick(10)
		s.move()
	# had sežere kostku - přidá se k hadovi a vygeneruje se nová
		if s.body[0].pos == snack.pos:
			s.addCube()
			snack = cube(randomSnack(rows, s), color=(255, 255, 255))

		for x in range(len(s.body)):
			# Kontrola kolize - když je pozice kostky na pozici již existují pozice hada, tak dojde ke srážce
			if s.body[x].pos in list(map(lambda z: z.pos,s.body[x + 1:])):
				print('Score: ', len(s.body))
				message_box('You Lost!', ' Score: {} \n Try again'.format(len(s.body)) )
				s.reset((10, 10))
				break

		redrawWindow(win)

	pass

main()
