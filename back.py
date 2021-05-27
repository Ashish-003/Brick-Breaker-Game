import numpy as np
from colorama import init,Fore, Back, Style
import os
from grid import Grid
#init(autoreset = True)
from config import *
#print(Fore.RED + 'Hi yalllll')

class Scenery:
    def __init__(self):
        # self._rows = rows
        # self._cols = cols*frames
        #self._grid = ([Back.BLACK + Fore.Black + ' ' for col in range(self._cols)])for rows in range self._rows])

        self._sky = Back.LIGHTMAGENTA_EX + " " + Back.RESET 
        self._ground = Back.LIGHTMAGENTA_EX + " " + Back.RESET
        # for val in range(self._cols):
        #     #upper
        #     self._grid[1][val] = Back.LIGHTMAGENTA_EX + " " + Back.RESET 
        #     #lower
        #     self._grid[self._rows -1][val] = Back.LIGHTMAGENTA_EX + " " + Back.RESET 
    def createGround(self, grid):
        grid[rows-1:rows, 0:columns] = self._ground
        grid[0:rows, 0:1] = self._ground

    def createSky(self, grid):
        grid[0, 0:columns] = self._sky
        grid[0:rows, columns-1:columns] = self._ground

#background = Scenery()
