#!/usr/bin/python2.7 -tt

import sys
import os

hex = "012345789abcdef"
val = 0

def Cat(filename):
	f = open(filename, 'rU')
	text = f.read()
	print text

#	for line in f:
#		print line,
#	f.close()


#standard out for main funtion
def main():
	args = sys,argv
	if len(sys.argv) > 1:
		for arg in args:
			Cat(sys.argv[arg])
	else:
		print 'Error you need an entry.'



# This is the standard boiler plate call for main
if __name__=='__main__':
	main()

