class Flowers:
	def __init__(self, name):
		self.name = name

	def color(self, color):
		print('{}: is {}'.format(self.name, color))

	def watering(self, water):
		print('{}: like {}'.format(self.name, water))

## Metoda grow() je bod č. 5: odvozené třídy budou mít stejnou metodu,
# která bude dělat stejnou věc jiným způsobem (koťátko mňouká, štěňátko štěká)

class Orchids(Flowers):
	def grow(self):
		print("{}: grow in the rainforest".format(self.name))

## bod č. 4: odvozená třída bude rozšiřovat metodu nadřazené třídy pomocí super()
	def watering(self, water):
		print('{}: are dry'.format(self.name))
		super().watering(water)

class Tulips(Flowers):
	def grow(self):
		print("{}: grow in spring".format(self.name))

class Cactus(Flowers):
	def grow(self):
		print("{}: grow in the desert".format(self.name))

## Bod č. 3: Jedna odvozená třída bude kompletně přepisovat metodu nadřazené třídy.
	def watering(self, water):
		print('{}: do not like {}'.format(self.name, water))


orchid = Orchids('Orchid')
orchid.grow()
orchid.watering('water')

tulips = Tulips('Tulips')
tulips.grow()
tulips.watering('water')

cactus = Cactus('Cactus')
cactus.grow()
cactus.watering('water')
