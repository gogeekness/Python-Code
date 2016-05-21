#!/usr/bin/python2.7 -tt

import sys
#from sys import argv


def main():
    if len(sys.argv) >= 2:
        script, filename = sys.argv
    else:
        print "Need file to parse."
        exit(1)
    print "Here's your file %r:" % filename
    n = 3    
    newlines = 0
    with open(filename) as f:
        f.seek(-1, 2)
        read_data = f.read(1)
        print "read data:", read_data
        flen = f.tell()+1
        while newlines < n:
            buff = f.read(1)
            print "buff read: ", buff
            while buff != "\n":
                if f.tell() == 0:
                    print "Start of File\n", f.read()
                    exit(2)
                f.seek(-2,1)
                buff = f.read(1)
                print buff
            newlines += 1
            f.seek(-2,1)
            print "newlines ", newlines
        blocklen = f.tell() - flen
        print "blocklen", blocklen
        buff = f.read(blocklen)
        print buff
    f.closed
    
    
        
# This is the standard boiler plate call for main
if __name__=='__main__':
        main()