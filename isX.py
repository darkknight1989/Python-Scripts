#!/usr/bin/env python

while True:
	print('Enter your age:')
	age = input()
	if age.isdecimal():
		break
	print('enter a whole number for your age')

while True:
	print('enter your password')
	password = input()
	if password.isalpha():
		break
	print('enter a text for your password')


