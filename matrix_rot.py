#!/usr/bin/python2.7 -tt

import sys
import random
from random import shuffle, randrange, randint

matrix = []
width = 5
height = 5

def print_val():
    for y in reversed(range(height-1)):      # [ [(T, T, T, T) ...][() () () () () ][][][][]  ] 
        initmatrix = "Row " + str(y) 
        #matrix.append([])
        for x in range(width-1):
            initmatrix = initmatrix + " Col " + str(x) + " => " + str(matrix[x][y]) 
        print(initmatrix)  

def main():
    for y in range(5):
        matrix.append([])
        for x in range(5):
            matrix[y].append(x+y)
    print matrix
    print_val()
    
    
    
# This is the standard boiler plate call for main
if __name__=='__main__':
        main()
