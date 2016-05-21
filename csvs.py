#!/usr/bin/python2.7 -tt


import sys
import string

cyph = open ("/home/gogeek/py-files/cypher", "r")
text = cyph.read()
out = ""

for x in range(0, len(text)):
	if str.isalpha(text[x]):
		y = ord(text[x])
		if (y - ord('x')) >  0:
			y = y - 26			
		out += chr(y+2)
	else:
		out += text[x]
print out		
		


