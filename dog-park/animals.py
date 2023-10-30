class Dog:

	scientific_name = "Canis lupus familiaris"

	def __init__(self, name):
		self.name = name
		self.barks = 0

	def speak(self):
		print("Woof!")

	def eat(self, food):
		if food == 'biscuit':
			print('Yummy')
		elif food == 'chair':
			print("That's not food!")

	def hear(self, words):
		if self.name in words:
			self.speak()
		else:
			print('...')

	def count(self):
		self.barks += 1
		for i in range(self.barks):
			self.speak()

	def do_trick(self):
		pass


class Husky(Dog):
	origin = "Siberia"

	def speak(self):
		print("Awooo!")

	def do_trick(self):
		print(f'{self.name} spins in the air and turns briefly into a chicken.')


class Chihuahua(Dog):
	def speak(self):
		print('Wiiii')


class Labrador(Dog):
	def speak(self):
		print('Wooo!')


class Cat:

	scientific_name = "Felis catus"

	def __init__(self):
		self.mood = "neutral"

	def speak(self):
		if self.mood == 'happy':
			print("Purrr")
		elif self.mood == "angry":
			print("Hisss!")
		elif self.mood == "neutral":
			print("Meow!")
