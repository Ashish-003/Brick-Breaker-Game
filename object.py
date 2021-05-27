from colorama import Fore, Back, Style
import numpy
import random
import os
from config import *
import config
from grid import Grid
global paddle
paddle = temp
bricks = [list("(^^^)")]
ball = [list("o")]
arr = []
power_arr = []
ship = [list("        _,--=--._                      "),
        list("             ,'    _    `.             "),
        list("            -    _(_)_o   -            "),
        list("       ____'    /_  _/]    `____       "),
        list("-=====::(+):::::::::::::::::(+)::=====-"),
        list("         (+).''''''''''''',(+)         "),
        list("             .           ,             "),
        list("               `  -=-  '               ")]


class item:
    def __init__(self):
        self.__height = 0
        self.__width = 0
        self._x = 0
        self._y = 0
        self._velx = 0
        self._vely = 0

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width


#################################################################################################################################################################################


class Paddle(item):
    def __init__(self):
        super().__init__()
        self.__height = len(paddle)
        self.__width = len(paddle[0])
        self._short = False
        self._long = False
        self.__time = 0
        self.__score = 0
        self._lives = 1500
        self.__level = 1

    def placePaddle(self, grid, x, y, paddle):
        self.clear(grid, paddle)
        self._x = x
        self._y = y - len(paddle[0])//2 + 1
        i = self._y
        for i in range(self._y, self._y+len(paddle[0])):
            grid[self._x][i] = Back.BLACK+Fore.GREEN + \
                paddle[0][i - self._y] + Fore.RESET

    def printPaddle(self, grid, paddle):
        for i in range(self._y, self._y+len(paddle[0])):
            grid[self._x][i] = Back.BLACK+Fore.GREEN + \
                paddle[0][i - self._y] + Fore.RESET

    def clear(self, grid, paddle):
        for i in range(self._y, self._y+len(paddle[0])):
            grid[self._x][i] = Back.BLACK + Fore.BLACK + ' '

    def dec_pos(self, grid, paddle):
        if(self._y > 2):
            self.clear(grid, paddle)
            self._y -= 2

    def inc_pos(self, grid, paddle):
        if(self._y < columns-len(paddle[0]) - 2):
            self.clear(grid, paddle)
            self._y += 2

    def getLives(self):
        return self._lives

    def getScore(self):
        return self.__score

    def changeScore(self, val):
        self.__score += val

    def getTime(self):
        return self.__time

    def changTime(self, val):
        self.__time += val

    def changlevel(self):
        self.__level += 1

    def getLevel(self):
        return self.__level

    def saaf(self, grid, paddle):
        for i in range(self._y+len(paddle[0]), self._y+len(paddle[0])+2):
            grid[self._x][i] = Back.BLACK + Fore.BLACK + ' '


##########################################################################################################


#########################################################################################################

class brick(item):
    def __init__(self):
        super().__init__()
        self.__height = len(bricks)
        self.__width = len(bricks[0])
        self._strength = 0
        self.exist = True
        self._points = 0
        self._exp = 0
        self._rain = False
        self._color1 = Back.BLUE + Fore.BLUE
        self._color2 = Back.RED + Fore.RED
        self._color3 = Back.YELLOW + Fore.YELLOW
        self._color4 = Back.WHITE + Fore.WHITE
        self._color5 = Back.CYAN + Fore.BLACK
        self._color = Back.BLACK + Fore.BLACK
        self.__stick = 1#random.randint(1, 15)//15
        self.__long = random.randint(1, 15)//15
        self.__short = random.randint(1, 15)//15
        self.__thru = random.randint(1, 15)//15
        self.__fast = random.randint(1, 15)//15
        self.__mul = random.randint(1, 15)//15
        self.power = self.__short + self.__long + \
            self.__stick + self.__thru + self.__fast + self.__mul

    def ifexist(self):
        return self.exist

    def ifrain(self):
        return self._rain

    def changeBrick(self, grid, object, Ball):

        # print(self.power)
        # print(score)
        # print(self._strength)
        if(self._exp == 1):
            for i in range(156, 162):
                arr[i].destroy(grid, object, Ball)
            for i in range(143, 150):
                arr[i].destroy(grid, object, Ball)
        if(self._strength == 1 or Ball.getThru() == True):
            self.destroy(grid, object, Ball)
        elif self._strength > 1:
            if(self.ifrain()):
                self._rain = False
                if(self._color == self._color3):
                    self._color = self._color2
                    self._strength = 3
                elif(self._color == self._color2):
                    self._color = self._color1
                    self._strength = 2
                else:
                    self._strength = 1
                    self.destroy(grid, object, Ball)
            else:
                if(self._color == self._color3):
                    self._color = self._color2
                else:
                    self._color = self._color1
            self._strength -= 1
            for k in range(self._y, self._y+len(bricks[0])):
                grid[self._x][k] = self._color + \
                    bricks[0][k-self._y] + Fore.RESET

    def printBrickx(self, grid):
        for k in range(self._y, self._y+len(bricks[0])):
            grid[self._x][k] = self._color + bricks[0][k-self._y] + Fore.RESET

    def destroy(self, grid, object, Ball):
        global no_brick
        object.changeScore(self._points)
        # print("hooo")
        # print(self.power)
        if(self.power != 0):
            os.system("aplay sounds/powerup.wav -q &")
            if(self.__stick == 1):
                p = powerups(self._x, self._y, 1, Ball._velx, Ball._vely)
                power_arr.append(p)
            elif(self.__long == 1):
                p = powerups(self._x, self._y, 2, Ball._velx, Ball._vely)
                power_arr.append(p)
            elif(self.__short == 1):
                p = powerups(self._x, self._y, 3, Ball._velx, Ball._vely)
                power_arr.append(p)
            elif(self.__thru == 1):
                p = powerups(self._x, self._y, 4, Ball._velx, Ball._vely)
                power_arr.append(p)
            elif(self.__fast == 1):
                p = powerups(self._x, self._y, 5, Ball._velx, Ball._vely)
                power_arr.append(p)
            elif(self.__mul == 1):
                p = powerups(self._x, self._y, 6, Ball._velx, Ball._vely)
                power_arr.append(p)

        if(self._strength > 0):
            config.no_brick = config.no_brick - 1
            print(config.no_brick)
        self.exist = False
        self._color = Back.BLACK + Fore.BLACK
        for k in range(self._y, self._y+len(bricks[0])):
            grid[self._x][k] = self._color + " " + Fore.RESET


class Brick1(brick):
    def __init__(self, x, y):
        super().__init__()
        self._color = self._color1
        self._strength = 1
        self._x = x
        self._points = 10
        self._y = y

    def printBrickx(self, grid):
        for k in range(self._y, self._y+len(bricks[0])):
            grid[self._x][k] = self._color1 + bricks[0][k-self._y] + Fore.RESET


class Brick2(brick):
    def __init__(self, x, y):
        super().__init__()
        self._color = self._color2
        self._strength = 2
        self._x = x
        self._points = 20
        self._y = y

    def printBrickx(self, grid):
        for k in range(self._y, self._y+len(bricks[0])):
            grid[self._x][k] = self._color2 + bricks[0][k-self._y] + Fore.RESET


class Brick3(brick):
    def __init__(self, x, y):
        super().__init__()
        self._color = self._color3
        self._strength = 3
        self._x = x
        self._points = 30
        self._y = y

    def printBrickx(self, grid):
        for k in range(self._y, self._y+len(bricks[0])):
            grid[self._x][k] = self._color3 + bricks[0][k-self._y] + Fore.RESET


class Brick4(brick):
    def __init__(self, x, y):
        super().__init__()
        self._color = self._color4
        self._strength = 0
        self._x = x
        self._y = y

    def printBrickx(self, grid):
        for k in range(self._y, self._y+len(bricks[0])):
            grid[self._x][k] = self._color4 + bricks[0][k-self._y] + Fore.RESET


class Brick5(brick):
    def __init__(self, x, y):
        super().__init__()
        self._color = self._color5
        self._strength = 0
        self._x = x
        self._y = y
        self._exp = 1

    def printBrickx(self, grid):
        for k in range(self._y, self._y+len(bricks[0])):
            grid[self._x][k] = self._color5 + bricks[0][k-self._y] + Fore.RESET


class Brick_rain(brick):
    def __init__(self, x, y):
        super().__init__()
        self._color = self._color3
        self._strength = 3
        self._rain = True
        self._points = 30
        self._x = x
        self._y = y

######################################################################################################################################


class Ball(item):
    def __init__(self):
        super().__init__()
        self.__height = len(ball)
        self.__width = len(ball[0])
        self.__onPaddle = True
        self.__tempx = 1
        self.__tempy = -1
        self.__stick = True
        self.__thru = False

    def changeThru(self, val):
        self.__thru = val

    def getThru(self):
        return self.__thru

    def changeStick(self):
        self.__stick = True

    def placeBall(self, grid, x, y, paddle):
        self._x = x-1
        self._loc = random.randint(0, len(paddle[0])-1)
        self.__onPaddle = True
        self.__tempx = 1
        self.__tempy = -1
        self._velx = 0
        self._vely = 0
        self.__stick = True
        self._y = y + self._loc

    def clear(self, grid):
        grid[self._x][self._y] = Back.BLACK + Fore.BLACK + ' '

    def stickBall(self, grid, y):
        if(self.__stick == True and self.__onPaddle == True):
            self.clear(grid)
            self._velx = 0
            self._vely = 0
            self._y = y + self._loc
            grid[self._x][self._y] = Fore.WHITE + ball[0][0]
            return 1
        return 0

    def start(self, grid):
        if(self.__stick == True and self.__onPaddle == True):
            self.__stick = False
            self.__onPaddle = False
            self._velx = self.__tempx
            self._vely = self.__tempy
            self.clear(grid)
            self._x += self._vely
            self._y += self._velx

    def printBall(self, grid):
        grid[self._x][self._y] = Back.BLACK+Fore.WHITE + ball[0][0]

    def checkWall(self):
        posx = self._x + self._vely
        posy = self._y + self._velx
        flag = 0
        if(posx < 1 and posy < 1):
            flag = 1
            self.__tempy = -self.__tempy
            self._vely = self.__tempy
            self.__tempx = -self.__tempx
            self._velx = self.__tempx
            self._x = 1-posx
            self._y = 1-posy
        elif(posx < 1 and posy > columns-2):
            flag = 1
            self.__tempy = -self.__tempy
            self._vely = self.__tempy
            self.__tempx = -self.__tempx
            self._velx = self.__tempx
            self._x = 1-posx
            self._y = columns-2 - (posy - columns+2)

        elif(posx < 1):
            flag = 1
            self.__tempy = -self.__tempy
            self._vely = self.__tempy
            self._y = posy
            self._x = 1-posx
        elif(posx > rows - 2):
            flag = 1
            self.__tempy = -self.__tempy
            self._vely = self.__tempy
            self._y = posy
            self._x = rows - 2 - (posx-rows+2)
        elif(posy < 1):
            flag = 1
            self.__tempx = -self.__tempx
            self._velx = self.__tempx
            self._x = posx
            self._y = 1-posy
        elif(posy > columns-2):
            flag = 1
            self.__tempx = -self.__tempx
            self._velx = self.__tempx
            self._x = posx
            self._y = columns-2 - (posy - columns+2)
        return flag

    def checkPaddle(self, object, x, y):
        flag = 0
        if(self._x == x-1 and (self._y >= y and self._y <= y + len(paddle[0]) - 1)):
            flag = 1
            h = self._y - y - len(paddle[0])//2 + 1
            self.__tempx += h
            self.__tempy = -1*self.__tempy
            if(self.__tempx > 2):
                self.__tempx = 2
            if(self.__tempx < -2):
                self.__tempx = -2
            self.__tempy = -1*self.__tempy
            if(self.__stick == True):
                self._velx = 0
                self._vely = 0
                self.__onPaddle = True
            else:
                self._velx = self.__tempx
                self._vely = self.__tempy
                self._x += self._vely
                self._y += self._velx
        elif(self._x == x and (self._y >= y and self._y <= y + len(paddle[0])-1)):
            flag = 1
            h = self._y - y - len(paddle[0])//2 + 1
            self.__tempx += h
            self.__tempy = -1*self.__tempy
            if(self.__tempx > 2):
                self.__tempx = 2
            if(self.__tempx < -2):
                self.__tempx = -2
            if(self.__stick == True):
                self._velx = 0
                self._vely = 0
                self.__onPaddle = True
            else:
                self._velx = self.__tempx
                self._vely = self.__tempy
                self._x += self._vely
                self._y += self._velx

        elif(self._x == x and (self._y < y or self._y > y + len(paddle[0]) - 1)):
            flag = 1
            object._lives -= 1
        return flag

    def checkBrick(self, grid, object):
        flag = 0
        posx = self._x + self._vely
        posy = self._y + self._velx
        minVal = min(self._y, posy)
        maxVal = max(self._y, posy)
        if maxVal == posy:
            maxVal += 1
        else:
            minVal -= 1
        for k in range(0, len(arr)):
            if(arr[k].ifexist()):
                start = arr[k].getY()
                end = start + len(bricks[0]) - 1
                startx = arr[k].getX()
                if posy > self._y:
                    if(start == self._y+1 and startx == self._x):
                        flag = 1
                        if(self.__thru == False):
                            self.__tempx = -1*self.__tempx
                            self._velx = self.__tempx
                        self._x += self._vely
                        self._y += self._velx
                        arr[k].changeBrick(grid, object, self)
                        break
                elif(posy < self._y):
                    if(end == self._y - 1 and startx == self._x):
                        flag = 1
                        if(self.__thru == False):
                            self.__tempx = -1*self.__tempx
                            self._vely = self.__tempy
                        self._velx = self.__tempx
                        self._x += self._vely
                        self._y += self._velx
                        arr[k].changeBrick(grid, object, self)
                        break
        if(flag == 0):
            for k in range(0, len(arr)):
                if(arr[k].ifexist()):
                    start = arr[k].getY()
                    end = start + len(bricks[0]) - 1
                    startx = arr[k].getX()
                    for i in range(minVal, maxVal):
                        if(startx == posx and i >= start and i <= end):
                            flag = 1
                            if(self.__thru == False):
                                self.__tempy = -1*self.__tempy
                                self._vely = self.__tempy
                            self._x += self._vely
                            self._y += self._velx
                            arr[k].changeBrick(grid, object, self)
                            break

        return flag
    def checkBoss(self, grid, boss):
        flag = 0
        posx = self._x + self._vely
        posy = self._y + self._velx
        minVal = min(self._y, posy)
        maxVal = max(self._y, posy)
        starty = boss.getY()
        endy = boss.getY()+len(ship[0]) - 1
        startx = boss.getX()
        endx = boss.getX() + len(ship) - 1
        # if posy > self ._y:
        #     if (startx == posx and )
        for i in range(minVal, maxVal+1):
            if((endx == posx or startx == posx) and i >= starty and i <= endy):
                flag = 1
                self.__tempy = -1*self.__tempy
                self._vely = self.__tempy
                self._x += self._vely
                self._y += self._velx
                boss.dec_health()
                return flag
        if posy > self._y:
            if(self._y <= starty and posy >= starty and self._y + 1 <= endy and self._x >= startx and self._x <= endx):
                flag = 1
                self.__tempx = -1*self.__tempx
                self._velx = self.__tempx
                self._x += self._vely
                self._y += self._velx
                boss.dec_health()
                return flag
        elif posy < self._y:
            if(self._y >= endy and posy <= endy and self._x >= startx and self._x <= endx):
                flag = 1
                self.__tempx = -1*self.__tempx
                self._velx = self.__tempx
                self._x += self._vely
                self._y += self._velx
                boss.dec_health()
                return flag

        return flag

    def move(self, grid, object, x, y, boss_flag, boss):
        self.clear(grid)
        if(self.checkWall()):
            os.system("aplay sounds/hitWall.wav -q &")
        elif(self.checkPaddle(object, x, y)):
            os.system("aplay sounds/hitPaddle.wav -q &")
            return True
        elif(self.checkBrick(grid, object)):
            os.system("aplay sounds/hitBrick.wav -q &")
        elif(boss_flag and self.checkBoss(grid, boss)):
            pass
        else:
            self._x += self._vely
            self._y += self._velx
        return False
        # print(self._vely)


#######################################################################################
class powerups(item):
    def __init__(self, x, y, val, velx, vely):
        super().__init__()
        self._x = x
        self._y = y
        self.__tempx = velx
        self._velx = velx
        self._char = str(val)
        self._exist = True
        self.__tempy = vely-0.8
        self._vely = vely-0.8

    def ifexist(self):
        return self._exist

    def clear(self, grid):
        grid[int(self._x)][int(self._y)] = Back.BLACK + Fore.BLACK + ' '

    def print(self, grid):
        grid[int(self._x)][int(self._y)] = Back.BLACK + \
            Fore.WHITE + self._char + Fore.RESET

    def changeexist(self):

        self._exist = False

    def getChar(self):
        return self._char

    def checkWall(self):
        self.__tempy = self._vely
        posx = self._x + self._vely
        posy = self._y + self._velx
        flag = 0
        if(posx < 2 and posy < 2):
            flag = 1
            self.__tempy = -self.__tempy
            self._vely = self.__tempy
            self.__tempx = -self.__tempx
            self._velx = self.__tempx
            self._x = 4-posx
            self._y = 4-posy
        elif(posx < 2 and posy > columns-3):
            flag = 1
            self.__tempy = -self.__tempy
            self._vely = self.__tempy
            self.__tempx = -self.__tempx
            self._velx = self.__tempx
            self._x = 4-posx
            self._y = columns-2 - (posy - columns+2)
        elif(posx < 2):
            flag = 1
            self.__tempy = -self.__tempy
            self._vely = self.__tempy
            self._y = posy
            self._x = 4-posx
        elif(posy < 2):
            flag = 1
            self.__tempx = -self.__tempx
            self._velx = self.__tempx
            self._x = posx
            self._y = 4-posy
        elif(posy > columns-3):
            flag = 1
            self.__tempx = -self.__tempx
            self._velx = self.__tempx
            self._x = posx
            self._y = columns-2 - (posy - columns+2)
        return flag


def move_power(grid):
    temp_arr = []
    global power_arr
    for i in range(len(power_arr)):
        if(power_arr[i].ifexist()):
            temp_arr.append(power_arr[i])
        else:
            power_arr[i].clear(grid)
    power_arr = temp_arr
    for i in range(len(power_arr)):
        power_arr[i].clear(grid)
        power_arr[i]._vely += 0.2
        if(power_arr[i].ifexist()):
            if(power_arr[i]._x >= rows-6):
                power_arr[i].changeexist()
            elif(power_arr[i].checkWall() == 0):
                power_arr[i]._x += power_arr[i]._vely
                power_arr[i]._y += power_arr[i]._velx
            power_arr[i].print(grid)


def check_power(grid, x, y):
    for i in range(len(power_arr)):
        if(power_arr[i].ifexist()):
            if((power_arr[i]._x == x or power_arr[i]._x == x-1 or power_arr[i]._x == x+1) and power_arr[i]._y >= y-1 and power_arr[i]._y <= y+len(paddle[0])+1):
                power_arr[i].changeexist()
                return power_arr[i].getChar()
    return '0'


def checkBricks(x):
    for i in range(len(arr)):
        if(arr[i].ifexist() and arr[i]._x == x):
            return True
    return False


def changeBrick(grid):
    for i in range(len(arr)):
        for k in range(arr[i]._y, arr[i]._y+len(bricks[0])):
            color = Back.BLACK + Fore.BLACK
            grid[arr[i]._x][k] = color + " " + Fore.RESET
    for i in range(len(arr)):
        arr[i]._x += 1


def placeBrick(grid):
    brickss = 0
    for i in range(rows//6, rows//2):
        for j in range(columns//6, 5*columns//6, len(bricks[0])):
            x = random.randint(1, 4)
            brickss += 1
            if(x == 1):
                Brick = Brick1(i, j)
            elif(x == 2):
                Brick = Brick2(i, j)
            elif(x == 3):
                Brick = Brick3(i, j)
            else:
                Brick = Brick4(i, j)
                brickss -= 1
            Brick.printBrickx(grid)
            arr.append(Brick)
    # print(str(no_brick) + " bricks")
    i = rows//2
    for j in range(columns//6, columns//6 + 6*len(bricks[0]), len(bricks[0])):
        Brick = Brick5(i, j)
        for k in range(Brick._y, Brick._y+len(bricks[0])):
            brickss += 1
            grid[Brick._x][k] = Brick._color + \
                bricks[0][k-Brick._y] + Fore.RESET
        arr.append(Brick)
    i = rows//2
    j = columns//6 + 7*len(bricks[0])
    brickss += 1
    Brick = Brick_rain(i, j)
    Brick.printBrickx(grid)
    arr.append(Brick)

    return brickss


def printBrick(grid):
    for i in range(len(arr)):
        if(arr[i].ifrain()):
            # print("yoooooo")
            if(arr[i]._color == arr[i]._color1):
                arr[i]._color = arr[i]._color2
            elif(arr[i]._color == arr[i]._color2):
                arr[i]._color = arr[i]._color3
            elif(arr[i]._color == arr[i]._color3):
                arr[i]._color = arr[i]._color1
        for k in range(arr[i].getY(), arr[i].getY() + len(bricks[0])):
            if(arr[i].ifexist()):
                grid[arr[i]._x][k] = arr[i]._color + \
                    bricks[0][k-arr[i]._y] + Fore.RESET
            else:
                grid[arr[i]._x][k] = arr[i]._color + " " + Fore.RESET


def delBricks(grid):
    color = Back.BLACK + Fore.BLACK
    global arr
    global temp
    temp = []
    for i in range(len(arr)):
        for k in range(arr[i].getY(), arr[i].getY() + len(bricks[0])):
            grid[arr[i]._x][k] = color + " " + Fore.RESET
    arr = temp
    power_arr = temp


def placenewBrick(grid, flag):
    # global arr
    if(flag == 1):
        Brick = Brick4(14, 7)
        Brick.printBrickx(grid)
        arr.append(Brick)
        Brick = Brick4(15, 80)
        Brick.printBrickx(grid)
        arr.append(Brick)
        Brick = Brick4(21, 64)
        Brick.printBrickx(grid)
        arr.append(Brick)
        Brick = Brick4(19, 40)
        Brick.printBrickx(grid)
        arr.append(Brick)
    # elif (flag == 2):
    #     i = 13
    #     Brick = Brick1(19, 20)
    #     Brick.printBrickx(grid)
    #     arr.append(Brick)
    #     # for j in range(columns//6, 5*columns//6, len(bricks[0])):
    #     # Brick = Brick1(19, 25)
    #     # Brick.printBrickx(grid)
    #     # arr.append(Brick)
    elif (flag == 3):
        i = 11
        for j in range(2*columns//6, 4*columns//6, len(bricks[0])):
            Brick = Brick1(i, j)
            Brick.power = 0
            Brick.printBrickx(grid)
            arr.append(Brick)
def placenewBrick_1(grid, flag):
    # Brick = Brick1(21, 40)
    # Brick.printBrickx(grid)
    # arr.append(Brick)
    for j in range(columns//6, 5*columns//6, len(bricks[0])):
        Brick = Brick1(11, j)
        Brick.power = 0
        Brick.printBrickx(grid)
        arr.append(Brick)