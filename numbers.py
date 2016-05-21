#!/usr/bin/python2.7 -tt
import sys
import os
import shutil

def main():
  args = sys.argv[1:]
  if len(sys.argv) > 2:
    numbers = map(int, args)
    a = numbers[0]
    b = numbers[1]
  
    print a , b
    if a > b :
      c = a
      a = b
      b = c
      print a, b
      
    for i in range(a, b+1):
      print i, i*i  
    
  else:
    print "Error there needs to be 2 integers."  

if __name__=='__main__':
  main()      


