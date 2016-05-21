#!/usr/bin/python2.7 -tt

import sys
import commands
import os

def List(dir):
	cmd = 'ls -l ' + dir
	print 'about to so this:' , cmd


	(status, output) = commands.getstatusoutput(cmd)
	if status:
		sys.stderr.write('There was an error:' + output)
		sys.exit(1) 
	print output	


#standard out for main funtion
def main():
	List(sys.argv[1])	

# This is the standard boiler plate call for main
if __name__=='__main__':
        main()


