#!/usr/bin/python3.4

from random import shuffle, randrange
import sys

 
def make_maze(w = 5, h = 5):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    vis2 = [0] * w + [1] 
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
    print (vis, vis2)
    print (ver)
    print (hor)
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        
        print(x, y, d)        
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: 
                hor[max(y, yy)][x] = "+  "
            if yy == y: 
                ver[y][max(x, xx)] = "   "
            walk(xx, yy)
 
    walk(randrange(w), randrange(h))
 
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s
 
if __name__ == '__main__':
    print(make_maze())