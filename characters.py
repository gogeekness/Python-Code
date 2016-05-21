#!/usr/bin/python2.7 -tt

import sys

def pald(num):
	print num
        for x in range(32, num):
          if (x % 30) == 0:
            print " "
          else:
            print chr(x),
	return num


def main():
	if len(sys.argv) > 1:
	        args = sys.argv[1:]
	        number = map(int, args)
	        if (number[0] > 255) | (number[0] < 32):
	          pald(255)
                else:
		  pald(number[0])
	else:
		print 'Error please enter a string.'
	

if __name__=='__main__':
	main()
