#!/usr/bin/python2.7 -tt

import sys
import numpy
import array

row = 12
col = 12

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')



def main():
	print tuple           # Prints complete list	
	print tuple[0]        # Prints first element of the list
	print tuple[1:3]      # Prints elements starting from 2nd to 4th
	print tuple[2:]       # Prints elements starting from 3rd element
	print tinytuple * 2   # Prints list two times
	print tuple + tinytuple # Prints concatenated lists



# This is the standard boiler plate call for main
if __name__=='__main__':
        main()

