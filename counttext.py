#!/usr/bin/python2.7 -tt

import sys
import commands
import os

def List(txt):
	d = ""
	cyph = open (txt, "r")
	txt = cyph.read()
	
	for w in range (0,len(txt)):
		if txt[w].isalpha():
			d = d + d.join(txt[w])	
	print d
	print w

#standard out for main funtion
def main():
	if len(sys.argv) == 2:
		List(sys.argv[1])
	else:
		print Enter_file
	

# This is the standard boiler plate call for main
if __name__=='__main__':
        main()

