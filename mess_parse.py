#!/usr/bin/python2.7 -tt

import sys
import os


def count_mess(filename):
	f = open(filename, 'rU')
	text = f.read()
	print len(text)

#standard out for main funtion
def main():
#        args = sys.argv
	if len(sys.argv) > 1:
		count_mess(sys.argv[1])
	else:
		print 'Error you need an entry.'



# This is the standard boiler plate call for main
if __name__=='__main__':
	main()

