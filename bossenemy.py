from colorama import Fore, Back, Style
# import numpy
import random
import os
# from config import *
import config
from grid import Grid
ship =[list("        _,--=--._                      "),                          
       list("             ,'    _    `.             "),
       list("            -    _(_)_o   -            "),
       list("       ____'    /_  _/]    `____       "),
       list("-=====::(+):::::::::::::::::(+)::=====-"),
       list("         (+).''''''''''''',(+)         "),
       list("             .           ,             "),
       list("               `  -=-  '               ")]
# bricks = [list("(^^^)")]
bomb_arr = []
class enemy:
    def __init__(self,x,y):
        self._x = x
        self._y = y
        self._health = 5
    def printboss(self,grid):
        # print(self._x)
        self.clear(grid)
        for i in range(self._x, self._x+len(ship)):
            for j in range(self._y, self._y+len(ship[0])):
                grid[i][j] = Back.BLACK + Fore.WHITE + ship[i-self._x][j-self._y] + Fore.RESET
    def clear(self,grid):
        for i in range(self._x, self._x+len(ship)):
            for j in range(self._y, self._y+len(ship[0])):
                grid[i][j] = Back.BLACK + Fore.BLACK + ' ' + Fore.RESET
    def inc_pos(self,grid):
        self.clear(grid)
        if(self._y<config.columns-len(ship[0])-2):
            self._y+=2
    def dec_pos(self,grid):
        self.clear(grid)
        if(self._y > 2):
            self._y -=2
    def getX(self):
        return self._x
    def dec_health(self):
        self._health -=1
    def getY(self):
        return self._y
class bombs:
    def __init__(self,x,y):
        self._x = x+len(ship)
        self._y = y + len(ship[0])//2
        self._velx = 1
        self.__exist = True
    def ifexist(self):
        return self.__exist
    def changeexist(self):
        self.__exist = False
    def print(self,grid):
        grid[int(self._x)][int(self._y)] = Back.RED + Fore.WHITE + '*' + Fore.RESET
    def clear(self, grid):
        grid[int(self._x)][int(self._y)] = Back.BLACK + Fore.BLACK + ' '
def dropBombs(x,y,grid):
    global bomb_arr
    bomb = bombs(x,y)
    bomb_arr.append(bomb)
    # print(len(bomb_arr))
def moveBombs(grid):
    global bomb_arr

    temp_arr = []
    for i in range(len(bomb_arr)):
        if(bomb_arr[i].ifexist()):
            temp_arr.append(bomb_arr[i])
        else:
            bomb_arr[i].clear(grid)
    bomb_arr = temp_arr
    for i in range(len(bomb_arr)):
        bomb_arr[i].clear(grid)
        if(bomb_arr[i].ifexist()):
            if(bomb_arr[i]._x >= config.rows-3):
                bomb_arr[i].changeexist()
            else:
                bomb_arr[i]._x += 1
            bomb_arr[i].print(grid)

def checkBombs(x,y):
    global bomb_arr
    for i in range(len(bomb_arr)):
        if(bomb_arr[i].ifexist()):
            if(bomb_arr[i]._x == x-1 and bomb_arr[i]._y >=y and bomb_arr[i]._y  <= y + 7):
                bomb_arr[i].changeexist()
                return True
    return False


