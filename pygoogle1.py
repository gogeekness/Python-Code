#!/usr/python2.7 -tt

import sys

def Hello(name):
	if name == 'Alice' or name == 'Nick':
		print 'Alart Alart:  Mode 0.'
		name = name + '???'
	else:
		print 'Else'
	name = name + '1111'
	print 'Hello', name

#standard out for main funtion
def main():
	if len(sys.argv) > 1:
		Hello(sys.argv[1])
	else:
		print 'Error you need an entry.'

# This is the standard boiler plate call for main
if __name__=='__main__':
	main()

