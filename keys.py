#!/usr/bin/python

birthdays = {'Josh': 'jun 20' , 'Raija': 'Apr 5' , 'Steve': 'Aug 17'}

while True:
	print('Enter a name: (blank to quit)')
	name = input()
	if name == '':
		break

	if name in birthdays:
		print(birthdays[name] + ' is birthday of ' + name)
	else:
	        print('I do not have birthday information for ' + name)
		print('When is their birthday?')
		bday = input()
	        birthdays[name] = bday
		print('birthday database updated')

