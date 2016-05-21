#!/usr/bin/python2.7 -tt

import sys
import os
import shutil

val = 0

def Cat(filename):
	try:
		f = open(filename, 'rU')
		text = f.read()
		print text
	except IOError:	
		print '************ IO Error', filename, ' *************'
	

#	for line in f:
#		print line,
#	f.close()


#standard out for main funtion
def main():
	args = sys.argv[1:]
	if len(sys.argv) > 1:
		for arg in args:
			Cat(arg)
	else:
		print 'Error you need an entry.'

# This is the standard boiler plate call for main
if __name__=='__main__':
	main()

