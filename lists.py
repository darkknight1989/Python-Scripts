#!/usr/bin/python

dogNames = []
while True:
	print('enter the names of dogs' + str(len(dogNames) + 1) + ' (Or enter nothing to stop):')
	name = input()
	if name == '':
		  break
	          dogNames = dogNames + [name]
	print('The dogNames are:')
	for name in dogNames:
	 	print(' ' + name)
