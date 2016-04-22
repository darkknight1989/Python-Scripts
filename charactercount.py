#!/usr/bin/env python

message = 'This week is going to be awesome week in the name of Jesus'
count = {}

for character in message:
	count.setdefault(character,0)
	count[character] = count[character] + 1

print(count)

