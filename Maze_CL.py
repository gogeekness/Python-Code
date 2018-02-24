#!/usr/bin/python2.7 -tt

#Maze Generator

from Maze_class import halls
import sys
#import pdb
import random
from random import randrange, randint

#Globals
#base maze 0 elemets

width = 0
height = 0
startx = 1
starty = 1


# test to see if the maze has any sealed cells


#standard out for main function
def main():
    #global width, height, maze, startx, starty
    random.seed()
    if len(sys.argv) == 3:
        width = int(str(sys.argv[1]))
        height = int(str(sys.argv[2]))
        if width < 2 and height < 2:
            print("Both values need to greater than 1.\n")
            sys.exit(1)
    else:
        print("Enter two numbers for width and height.\n")
        sys.exit(1)

    maze1 = halls()    #Init object maze1
    mazegood = False

    while not mazegood:
        startx = random.randint(0, width-1)
        starty = random.randint(0, height-1)
        #print_val()
        maze1.seal_halls(width, height)  #initial maze all cells clossed
        maze1.build_maze(startx, starty, width, height)
        mazegood = maze1.test_maze(width, height)
    maze1.solve(0, 0, width, height)
    #for (x,y) in solve_path:
    #    maze[x][y][4] = True
    maze1.print_maze(width, height)

# This is the standard boiler plate call for main
if __name__=='__main__':
        main()