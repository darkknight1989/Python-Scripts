#!/usr/bin/env python

import random
def getnum(answer):
	if answer == 1:
		return 'it is certain'
	elif answer == 2:
		return 'it is decidedly so'
	elif answer == 3: 
		return 'it is good'
	elif answer == 4:
		return 'Good on you'

r = random.randint(1, 4)

fortune = getnum(r)

print(fortune)
