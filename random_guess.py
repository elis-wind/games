import random

print("\nGuess the number between 1 and 20!!\n")

number = random.randint(1, 20)
guess = 0

while guess != number:
	guess = int(input('Your guess: '))
	if guess < number:
		print("Your number is too small")
	if guess > number:
		print("Your number is too big")
else:
	print('Congratulations! You made it!')
