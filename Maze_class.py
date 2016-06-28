#Maze classes for Maze gen.py

class halls:
    
    #Set init for the Maze
    def __init__(self):
        self.data = []
        
    #reseal the halls in the maze
    def seal_halls(self, width, height):
        self.data = [[[False, False, False, False, False] for y in range(height)] for x in range(width)]
        
    def open_doors(self, x, y, xx, yy):
        #outxxyy = "X Y:" + str(x) + " " + str(y) + "  XX YY:" + str(xx) + " " + str(yy) 
        #sys.stdout.write(outxxyy)
        if xx == 1: #EAST
            self.data[x][y][1] = True
            self.data[x + xx][y][3] = True
            #print(" East")
        elif xx == -1: #WEST
            self.data[x][y][3] = True
            self.data[x + xx][y][1] = True
            #print(" West")
        elif yy == 1: #NORTH    
            self.data[x][y][0] = True
            self.data[x][y + yy][2] = True
            #print(" North")
        elif yy == -1: #SOUTH
            self.data[x][y][2] = True
            self.data[x][y + yy][0] = True
            #print(" South")
            # For viewing the data set for maze   
    
    def sealed_cell(self, cellx, celly, width, height):
        if cellx in range(width) and celly in range(height):
        # are all door closed?
            if any(self.data[cellx][celly]) == False:
                return "sealed"
            else:   
                return "opened"
        else:
        #out of bounds are always sealed
            return "bounds"
            
    def print_maze(self, width, height):
    # display u\2588 block char
    # directions for NORTH, EAST, SOUTH, WEST
        print(u'\u2588' * (3 * width + 1))
        for y in reversed(range(height)):
            cellew = u'\u2588'
            for x in range(width):      # [ [(T, T, T, T) ...][() () () () () ][][][][]  ] 
                if self.data[x][y][1]:  #If there is a EAST opening
                    if self.data[x][y][4]:
                        cellew = cellew + " * "
                    else:
                        cellew = cellew + "   "
                else:   
                    if self.data[x][y][4]:
                        cellew = cellew + " *" + u'\u2588'
                    else:
                        cellew = cellew + "  " + u'\u2588'
            print(cellew)
            cellns = u'\u2588'
            for x in range(width):  
                if self.data[x][y][2]:  #Is there is a SOUTH opening
                    cellns = cellns + "  " + u'\u2588'
                else:   
                    cellns = cellns + (3 * u'\u2588') 
            print(cellns)     
                
    def solve(self, x, y, width, height):
        # directions for NORTH, EAST, SOUTH, WEST
        # F(n) = Goal
        # print("Start Solve", x, y, self.data[x][y][4])
        if x == (width - 1) and y == (height - 1):
            self.data[x][y][4] = True
            return True
        if self.sealed_cell(x, y, width, height) != "opened" or self.data[x][y][4] == True:
            return False
        self.data[x][y][4] = True  #Key entry, need to set breadcrumbs
        if self.data[x][y][0] == True and self.solve(x, y+1, width, height):
            return True
        if self.data[x][y][1] == True and self.solve(x+1, y, width, height):
            return True
        if self.data[x][y][2] == True and self.solve(x, y-1, width, height): 
            return True          
        if self.data[x][y][3] == True and self.solve(x-1, y, width, height):
            return True 
        self.data[x][y][4] = False 
        return False      
 
            
            
    