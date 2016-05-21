#!/usr/bin/python2.7 -tt

import sys


#def parse(file):
	#directory
	


#standard out for main funtion
def main():
	if len(sys.argv) != 2:
		print "Need file."
	else:
		print sys.argv[1]
		parse = open(sys.argv[1],'r')
		txtblock = parse.read()
		print len(txtblock)
		print txtblock

# This is the standard boiler plate call for main
if __name__=='__main__':
        main()


