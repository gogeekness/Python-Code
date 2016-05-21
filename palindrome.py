#!/usr/bin/python2.7 -tt

import sys

def pald(text):
	print text
	print text[::-1]
	if text == text[::-1]:
		print "correct"
	return text


def main():
	if len(sys.argv) > 1:
		pald(sys.argv[1])
	else:
		print 'Error please enter a string.'
	

if __name__=='__main__':
	main()
