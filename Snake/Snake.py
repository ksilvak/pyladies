from Cube import cube
import pygame


class snake(object):
	body = []
	turns = {}
	def __init__(self, color, pos):
		self.color = color
		self.head = cube(pos)
		self.body.append(self.head)
		self.dirnx = 0
		self.dirny = 1

	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			keys = pygame.key.get_pressed()

	## 	Tvořím nový dictionary turns, kde klíč je [self.head.pos[:]] = aktuální pozice hlavy hada,
	# která se rovná dirny a , takže vím, kterým směrem se had pohnul

			for key in keys:
				if keys[pygame.K_LEFT]:
					self.dirnx = -1
					self.dirny = 0
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

				elif keys[pygame.K_RIGHT]:
					self.dirnx = 1
					self.dirny = 0
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

				elif keys[pygame.K_UP]:
					self.dirnx = 0
					self.dirny = -1
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

				elif keys[pygame.K_DOWN]:
					self.dirnx = 0
					self.dirny = 1
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

## Vezmu index(i) a cube objekt(c) v self.body, cube objekt má nějakou pozici (p),
# podívám se, jestli je ta pozice v turns, když tam je, tak se had pohne
# k pohybu použiju index té pozice(p) a vytvořím cube.move() z této uložené pozice (turn[0] = x, turn[1] = y  )
# když je index(i) rovno délce self.body - 1, znamená to, že jsem na poslední kostce. Musím odstranit turn,
# jinak had automaticky změní směr.
#Když pozice v turns není, tak zkontroluji jestli je na okraji obrazovky

		for i, c in enumerate(self.body):
			p = c.pos[:]
			if p in self.turns:
				turn = self.turns[p]
				c.move(turn[0],turn[1])
				if i == len(self.body) - 1:
					self.turns.pop(p)
			else:
				if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1]) # jede vlevo, dostane se nakonec, změním pozici na pravou stranu obrazovky
				elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1]) # jede vpravo, dostane se nakonec, změním pozici na levou stranu obrazovky
				elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0) # jede dolu, dostane se nakonec, změním pozici nahoru
				elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1) # jede nahoru, dostane se nakonec, změním pozici dolu
				else: c.move(c.dirnx,c.dirny) # pokračuje v pohybu

	def reset(self, pos):
		self.head = cube(pos)
		self.body = []
		self.body.append(self.head)
		self.turns = {}
		self.dirnx = 0
		self.dirny = 1

	def addCube(self):
		tail = self.body[-1] #najdu pozici ocásku - poslední element
		dx, dy = tail.dirnx, tail.dirny

## Zkontroluju jakým směrem se had hýbe, takže vím, kam umístit novou kostku - kostky se nebudou překrývat

		if dx == 1 and dy == 0:
			self.body.append(cube((tail.pos[0]-1, tail.pos[1])))
		elif dx == -1 and dy == 0:
			self.body.append(cube((tail.pos[0]+1, tail.pos[1])))
		elif dx == 0 and dy == 1:
			self.body.append(cube((tail.pos[0], tail.pos[1]-1)))
		elif dx == 0 and dy == -1:
			self.body.append(cube((tail.pos[0], tail.pos[1]+1)))

		# kostka se nehýbe, musím jí nastavit směr
		self.body[-1].dirnx = dx
		self.body[-1].dirny = dy

	def draw(self, surface):
		for i, c in enumerate(self.body):
			# musím najít první kostku, parametr True ji nakreslí oči
			if i ==0:
				c.draw(surface, True)
			else:
				c.draw(surface)
