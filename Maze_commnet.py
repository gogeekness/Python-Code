#!/usr/bin/python2.7 -tt

#Maze Generator

import sys
#import pdb
import random
from random import shuffle, randrange, randint

#Globals
#base maze 0 elemets
maze = []
width = 0
height = 0
startx = 1
starty = 1

# directions for NORTH, EAST, SOUTH, WEST
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

#---------------------------------------------------------
# False --> blocked
# maze[0].append((True, False, False, True))
#                 NORTH, EAST, SOUTH, WEST
#---------------------------------------------------------

# create the data set of cells with all of the cells closed off each other.
def initial_maze(width, height):
    global maze          #The initial
    maze = [[[False, False, False, False, False] for y in range(height)] for x in range(width)]
    return maze     
          
#To see if in bounds, if not treat as 'opened' cell and not use
#To test if the cell is sealed off completely 
def sealed_cell(cellx,celly):
    if cellx in range(width) and celly in range(height):
        # are all door closed?
        if any(maze[cellx][celly]) == False:
            return "sealed"
        else:   
            return "opened"
    else:
        #out of bounds are always sealed
        return "bounds"

# test to see if the maze has any sealed cells
def test_maze(width, height):
    for y in range(height):   
        for x in range(width):
            #print("Testing x y:" + str(x) + " " + str(y) + " " + sealed_cell(x,y))
            if sealed_cell(x,y) == "sealed":
                return False
    return True        
    
def open_doors(x,y, xx, yy):
    # directions for NORTH, EAST, SOUTH, WEST
    global maze
    #outxxyy = "X Y:" + str(x) + " " + str(y) + "  XX YY:" + str(xx) + " " + str(yy) 
    #sys.stdout.write(outxxyy)
    if xx == 1: #EAST
        maze[x][y][1] = True
        maze [x + xx][y][3] = True
        #print(" East")
    elif xx == -1: #WEST
        maze[x][y][3] = True
        maze [x + xx][y][1] = True
        #print(" West")
    elif yy == 1: #NORTH    
        maze[x][y][0] = True
        maze [x][y + yy][2] = True
        #print(" North")
    elif yy == -1: #SOUTH
        maze[x][y][2] = True
        maze [x][y + yy][0] = True
        #print(" South")
        # For viewing the data set for maze    
        
def print_val():
    for y in reversed(range(height)):      # [ [(T, T, T, T) ...][() () () () () ][][][][]  ] 
        initmaze = "Row " + str(y) 
        maze.append([])
        for x in range(width):
            initmaze = initmaze + " Col " + str(x) + " " + str(maze[x][y]) 
        print(initmaze)     
        
def print_maze():
    # display u\2588 block char
    # directions for NORTH, EAST, SOUTH, WEST
    print(u'\u2588' * (3 * width + 1))
    for y in reversed(range(height)):
        cellew = u'\u2588'
        for x in range(width):      # [ [(T, T, T, T) ...][() () () () () ][][][][]  ] 
            if maze[x][y][1]:  #If there is a EAST opening
                if maze[x][y][4]:
                    cellew = cellew + " * "
                else:
                    cellew = cellew + "   "
            else:   
                if maze[x][y][4]:
                    cellew = cellew + " *" + u'\u2588'
                else:
                    cellew = cellew + "  " + u'\u2588'
        print(cellew)
        cellns = u'\u2588'
        for x in range(width):  
            if maze[x][y][2]:  #Is there is a SOUTH opening
                cellns = cellns + "  " + u'\u2588'
            else:   
                cellns = cellns + (3 * u'\u2588') 
        print(cellns)        
        
def build_maze(x,y):
    shuffle(directions)
    for (xx, yy) in directions:
        #print("Cell x y:",x ,y,"  Added directions to x y:", x + xx, y + yy, "Limits ", width, height)
        tested = sealed_cell(x + xx, y + yy)
        if tested == "sealed": 
            open_doors(x, y, xx, yy)
            #print_val()
            #print("Good Cell:",x ,y, "Direction", xx, yy, "Added directions", x + xx, y + yy, " result:", tested, " Num: ", num )
            build_maze(x + xx, y + yy)  
 
def solve(x,y):
    # directions for NORTH, EAST, SOUTH, WEST
    # F(n) = Goal
    global maze
    print("Start Solve", x, y)
    if x == (width - 1) and y == (height - 1):
        maze[x][y][4] = True
        print("Found Goal", x, y, maze[x][y][4])
        return True
    if sealed_cell(x, y) != "opened" or maze[x][y][4] == True:
        print("Not Opened or Pathed", x, y, maze[x][y][4])
        return False
    maze[x][y][4] = True
    if maze[x][y][0] == True and solve(x, y+1):
        print("NORTH ",x,y, maze[x][y][4])
        return True
    if maze[x][y][1] == True and solve(x+1, y):
        print("EAST ",x,y, maze[x][y][4])
        return True
    if maze[x][y][2] == True and solve(x, y-1): 
        print("SOUTH ",x,y, maze[x][y][4])
        return True          
    if maze[x][y][3] == True and solve(x-1, y):
        print("WEST ",x,y, maze[x][y][4])
        return True 
    maze[x][y][4] = False 
    print("No Direction", x, y, maze[x][y][4])
    return False   
   
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
    mazegood = False
    while not mazegood:
        startx = random.randint(0, width-1)
        starty = random.randint(0, height-1)
        maze = initial_maze(width, height)  #initial maze all cells clossed
        #print_val()
        build_maze(startx, starty)    
        mazegood = test_maze(width, height)
    solve(0,0)
    #for (x,y) in solve_path:
    #    maze[x][y][4] = True
    print_maze()
   
# This is the standard boiler plate call for main
if __name__=='__main__':
        main()