#!/usr/bin/python2.7 -tt

import sys

hex = "0123456789abcdef"
Total = 0

def Find_hex(char):
	global hex
	val = hex.find(char)
	return val

def Find_number(name):
	global Total, val     
	print name
	for i in name:
		Total = (Total * 16) + Find_hex(i)      
	return Total	

#standard out for main funtion
def main():
        if len(sys.argv) > 1:
                print 'Total is:',Find_number(sys.argv[1])
        else:
                print 'Error you need an entry.'


# This is the standard boiler plate call for main
if __name__=='__main__':
        main()
