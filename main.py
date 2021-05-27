import signal, os, time
from back import Scenery
from grid import Grid 
from config import *
import config
from colorama import Fore, Back, Style
from input import *
from game_over import *
from object import *
from bossenemy import *

def move (y, x):
	print("\033[%d;%dH" % (y, x))


#################################################
os.system('clear')
gridObj = Grid(rows, columns)
Paddle = Paddle()
Paddle.placePaddle(gridObj.getMatrix(),edge,columns//2,paddle)
Ball = Ball()
Ball.placeBall(gridObj.getMatrix(),Paddle.getX(),Paddle.getY(),paddle)
config.no_brick =  placeBrick(gridObj.getMatrix())
# print(no_brick)
Boss = enemy(3,columns//4+7)
sceneryObj = Scenery()
getch= Get()
getch.hide_cursor()
x = 1
y = 1
# def clear():
# 	print(clrscr)
sceneryObj.createGround(gridObj.getMatrix())
sceneryObj.createSky(gridObj.getMatrix())
start_time = time.time()
os.system('stty -echo')
long_time = 0
short_time = 0
thru_time = 0
fast_time = 0
level_time = 0
prev_time = 0
brick_flag = False
Coll_flag = False
long_flag = False
short_flag = False
fast_flag = False
thru_flag = False
boss_flag = False
bomb_flag = False
layer_1 = False
layer_2 = False
flag = 1
arg = 0.09
def resetPower():
	# print("here")
	global long_flag,short_flag,fast_flag,thru_flag,level_time,arg,paddle,temp,paddle_long
	long_flag = False
	short_flag = False
	fast_flag = False
	thru_flag = False
	level_time = 0
	arg = 0.09
	# print(paddle)
	paddle = temp
	Paddle.saaf(gridObj.getMatrix(),paddle)
	Ball.clear(gridObj.getMatrix())
	Ball.changeThru(False)
	delBricks(gridObj.getMatrix())
	

while True:
	#print(no_brick)
	# print(long_time)
	# print(paddle[0],end = '\n')
	key_inp = input_to(getch,arg)
	
	move(2,0)
	before = Paddle.getLives()
	print(Fore.WHITE+Style.BRIGHT+ "Time Elapsed: %3d "%(Paddle.getTime()), end = '\t\t')
	print("Level: %d"%Paddle.getLevel(),end = '\t')
	print("Lives: %4d" %Paddle.getLives(), end = '\t')
	print("Score:", Paddle.getScore(), end = '\t')
	if (boss_flag):
		print("Boss_health:", Boss._health, end = '')
	print(end = '\n')

	if(before == 0 or brick_flag or bomb_flag):
		loss_game()
		getch.show_cursor()
		os.system('stty echo')
		quit()
	if(Boss._health == 6):
		win_game()
		getch.show_cursor()
		os.system('stty echo')
		quit()
	if(config.no_brick == 0):
		if(Paddle.getLevel()==4):
			win_game()
			getch.show_cursor()
			os.system('stty echo')
			quit()
		resetPower()
		Paddle.changlevel()
		if(Paddle.getLevel()<=3):
			Paddle.placePaddle(gridObj.getMatrix(),edge,columns//2,paddle)
			Ball.placeBall(gridObj.getMatrix(),Paddle.getX(),Paddle.getY(),paddle)
			config.no_brick =  placeBrick(gridObj.getMatrix())
		else:
			boss_flag = True
			placenewBrick(gridObj.getMatrix(),1)
			Boss.printboss(gridObj.getMatrix())
			Paddle.placePaddle(gridObj.getMatrix(),edge,columns//2,paddle)
			Ball.placeBall(gridObj.getMatrix(),Paddle.getX(),Paddle.getY(),paddle)
	# if(Boss._health <5 and not layer_1):
	# 	placenewBrick_1(gridObj.getMatrix(),2)
	# 	layer_1 = True
	if(Boss._health <4 and not layer_2):
		layer_2 = True
		placenewBrick(gridObj.getMatrix(),3)
	if(prev_time<level_time and level_time>1 and Coll_flag and not boss_flag):
		# bricks fall
		changeBrick(gridObj.getMatrix())
	if(prev_time<level_time and boss_flag==True and level_time%5==0):
		dropBombs(Boss.getX(),Boss.getY(),gridObj.getMatrix())
	printBrick(gridObj.getMatrix())
	char = check_power(gridObj.getMatrix(),Paddle.getX(),Paddle.getY())
	if(boss_flag):
		bomb_flag = checkBombs(Paddle.getX(),Paddle.getY())
	move_power(gridObj.getMatrix())
	Ball.printBall(gridObj.getMatrix())
	if(boss_flag):
		Boss.printboss(gridObj.getMatrix())
		moveBombs(gridObj.getMatrix())
	Paddle.printPaddle(gridObj.getMatrix(),paddle)
	if(char == '1'):
		Ball.changeStick()
	if(char == '2'):
		long_flag = True
		long_time = start_time+10
		paddle = paddle_long
		#print(paddle[0])print(prev_time)
	if(char == '3'):
		short_time = start_time+10
		paddle = paddle_short
		short_flag = True
		Paddle.saaf(gridObj.getMatrix(),paddle)
	if(char == '4'):
		fast_time = start_time+15
		fast_flag = True
		arg = 0.05
	if(char == '5'):
		thru_time = start_time+10
		thru_flag = True
		Ball.changeThru(True)

	
	gridObj.printView()
	# print("helooooooooo" + str(char))
	prev_time = level_time
	if(time.time()- start_time>=1):
		start_time += 1
		level_time += 1
		Paddle.changTime(1)
	if(key_inp != None):
		if(key_inp == 'q' or key_inp == 'Q'):
			loss_game()
			getch.show_cursor()
			os.system('stty echo')
			quit()
		elif(key_inp == 'a' or key_inp == 'A'):
			Boss.dec_pos(gridObj.getMatrix())
			Paddle.dec_pos(gridObj.getMatrix(),paddle)
			x = Ball.stickBall(gridObj.getMatrix(),Paddle.getY())
		elif(key_inp == 'd' or key_inp == 'D'):
			Boss.inc_pos(gridObj.getMatrix())
			Paddle.inc_pos(gridObj.getMatrix(),paddle)
			y = Ball.stickBall(gridObj.getMatrix(),Paddle.getY())
		elif(key_inp == ' '):
			Ball.start(gridObj.getMatrix())
			flag = 0
		# flag = x or y
		elif(key_inp == 'n' or key_inp == 'N'):
			if(Paddle.getLevel()==4):
				loss_game()
				getch.show_cursor()
				os.system('stty echo')
				quit()
			resetPower()
			Paddle.changlevel()
			if(Paddle.getLevel()<4):
				Paddle.placePaddle(gridObj.getMatrix(),edge,columns//2,paddle)
				Ball.placeBall(gridObj.getMatrix(),Paddle.getX(),Paddle.getY(),paddle)
				config.no_brick =  placeBrick(gridObj.getMatrix())
			else:
				boss_flag = True
				placenewBrick(gridObj.getMatrix(),1)
				Boss.printboss(gridObj.getMatrix())
				Paddle.placePaddle(gridObj.getMatrix(),edge,columns//2,paddle)
				Ball.placeBall(gridObj.getMatrix(),Paddle.getX(),Paddle.getY(),paddle)
			
	Coll_flag = False
	if(flag == 0):
		Coll_flag =  Ball.move(gridObj.getMatrix(),Paddle,Paddle.getX(),Paddle.getY(),boss_flag,Boss)
	if(long_flag == True and long_time<start_time):
		long_flag = False
		paddle = temp
		Paddle.saaf(gridObj.getMatrix(),paddle)
	if(short_flag == True and short_time<start_time):
		short_flag = False
		paddle = temp
	if(fast_flag == True and fast_time<start_time):
		short_flag = False
		arg = 0.09
	if(thru_time<start_time and thru_flag == True):
		thru_flag = False
		Ball.changeThru(False)
	brick_flag = checkBricks(edge)
	now_live = Paddle.getLives()
	if(now_live<before):
		time.sleep(1)
		flag = 1
		Paddle.placePaddle(gridObj.getMatrix(),edge,columns//2,paddle)
		Ball.placeBall(gridObj.getMatrix(),Paddle.getX(),Paddle.getY(),paddle)
getch.show_cursor()
