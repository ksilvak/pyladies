class Animal:
	def __init__(self, name):
		self.name = name

	def eat(self, food):
		print("{}: I like {}!".format(self.name, food))

class Kitten(Animal):
	def meow(self):
		print("{}: MŇAU MŇAU!".format(self.name))

	def eat(self, food):
		print("({}: look at {})".format(self.name, food))
		super().eat(food)

class Puppy(Animal):
	def woof(self):
		print("{}: ŠTĚK ŠTĚK!".format(self.name))

class Horse(Animal):
	def noise(self):
		print("{}: ŘECHT ŘECHT!".format(self.name))

baby = Kitten('Baby')
azor = Puppy('Azor')
dafne = Horse('Dafne')
baby.meow()
azor.woof()
dafne.noise()
baby.eat('mouse')
azor.eat('bone')
dafne.eat('grass')
