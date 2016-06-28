#!/usr/bin/python2.7 -tt

#Maze Generator

from Maze_class import halls
import sys
#import pdb
import random
from random import shuffle, randrange, randint

#Globals
#base maze 0 elemets

width = 0
height = 0
startx = 1
starty = 1

# directions for NORTH, EAST, SOUTH, WEST
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

#---------------------------------------------------------
# False --> blocked
# maze[0].append((True, False, False, True, True))
#                 NORTH, EAST, SOUTH, WEST, was here
#---------------------------------------------------------

# test to see if the maze has any sealed cells
def test_maze(maze1, width, height):
    for y in range(height):   
        for x in range(width):
            #print("Testing x y:" + str(x) + " " + str(y) + " " + sealed_cell(x,y))
            if maze1.sealed_cell(x, y, width, height) == "sealed":
                return False
    return True        
       
        
def build_maze(maze1, x, y):
    shuffle(directions)
    for (xx, yy) in directions:
        #print("Cell x y:",x ,y,"  Added directions to x y:", x + xx, y + yy, "Limits ", width, height)
        tested = maze1.sealed_cell(x + xx, y + yy, width, height)
        if tested == "sealed": 
            maze1.open_doors(x, y, xx, yy)
            #print_val()
            #print("Good Cell:",x ,y, "Direction", xx, yy, "Added directions", x + xx, y + yy, " result:", tested, " Num: ", num )
            build_maze(maze1, x + xx, y + yy)  
   
#standard out for main function
def main():
    global width, height, maze, startx, starty
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
        build_maze(maze1, startx, starty)    
        mazegood = test_maze(maze1, width, height)
    maze1.solve(0, 0, width, height)
    #for (x,y) in solve_path:
    #    maze[x][y][4] = True
    maze1.print_maze(width, height)
   
# This is the standard boiler plate call for main
if __name__=='__main__':
        main()