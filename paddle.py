from colorama import Fore, Back, Style
import numpy
import random
import os
from config import *
from object import *
from grid import Grid 
temp = [list("(^^^^^)")]
paddle_short = [list("(^^^)")]
paddle_long = [list("(^^^^^^^)")]
paddle = paddle_long
class item:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._height = 0
        self._width = 0
        self._velx =  0
        self._vely = 0
    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getHeight(self):
        return self._height
    
    def getWidth(self):
        return self._width
####################################################################

class Paddle(item):
    def __init__(self):
        super().__init__()
        self._height = len(paddle)
        self._width = len(paddle[0])
        self._short = False
        self._long = False
        self._time = 0
        self._score = 0
        self._lives = 3

        
    def placePaddle(self,grid,x,y):
        self.clear(grid)
        self._x = x
        self._y = y - len(paddle[0])//2 +1
        for i in range(self._y,self._y+len(paddle[0])):
            grid[self._x][i] = Back.BLACK+Fore.GREEN + paddle[0][i - self._y] + Fore.RESET
    def printPaddle(self,grid):   
        for i in range(self._y,self._y+len(paddle[0])):
            grid[self._x][i] = Back.BLACK+Fore.GREEN + paddle[0][i - self._y] + Fore.RESET
    def clear(self,grid):
        for i in range(self._y,self._y+len(paddle[0])):
                grid[self._x][i] = Back.BLACK+ Fore.BLACK + ' ' 
    def dec_pos(self,grid):
        if(self._y> 2 ):
            self.clear(grid)
            self._y -= 2
    def inc_pos(self,grid):       
        if(self._y < columns-len(paddle[0])-1) :
            self.clear(grid)
            self._y += 2
    def getLives(self):
        return self._lives
    def getScore(self):
        return self._score
    def changTime(self,val):
        self._time += val
