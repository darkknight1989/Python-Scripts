#!/usr/bin/env python

import random
secret = random.randint(1, 20)
print('Im thinking of a number between 1 and 20')

for guessrange in range(1, 7):
	print('take a guess')
	guess = int(input())

	if guess < secret:
		print('your number is too low')
	if guess > secret:
		print('your number is too high')
	else:
		break

if guess == secret:
	print('Good on you' + str(guessrange) + ' guesses')

else:
	print('another try mate' +  str(secret))

