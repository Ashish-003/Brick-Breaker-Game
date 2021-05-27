# Brick-Breaker-Game
A terminal Game in Python3 
# ARCADE GAME - Brick Breaker

This is an arcade game in Python3 (terminal-based), of brick breaker game. In this the player operates the paddle to bounce the ball to destroy the bricks.

## Installation

Colorama library:
```
pip3 install colorama
```
Numpy library
```
pip3 nstall numpy
```
## Run
```
python3 main.py
```

## Controls
### ` a` or `A` - paddle moves towards left.
### `d` or `D` - paddle moves towards right.
### `n` or `N` - Moves to next Level
### `q` or `Q` - Quit the game.
### `<space>` - release the ball.

## Rules and Features


- Player has one paddle. In the starting the player can control the ball release.Ball respawns on randomn spot on the Paddle

- Player loose a life on when ball goes below the paddle

- After the ball get released. If it collides with wall it get delflected by wall in the opposite direction.

- If the ball collides with bricks, bricks looses its strength changes its color and reflect the ball.

- Player gets points on hitting the brick.

- The colors of the bricks are according to strength. 
BLUE - 1, RED - 2, YELLOW - 3, WHITE - Unbreakable, CYAN - Explosive

- If the ball collides with the paddle it will get deflected acoording to the position of paddle.

-Final level consists of boss enemy (ufo) which drops bombs.Collecting bombs leads to  loss in game

## Concept Used

The main concept used in this OOPS concept.

### Inheritance

Classes in bricks inherit from the parent class Brick.

### Polymorphism

Functions such as printBrickx() in Brick uses polymorphism.



### Abstraction

Functions such as clear(), checkPaddle(), checkWall() in Ball uses.

### Encapsulation

Classes and objects based approach is used which makes this program more modular and hence encapsulation is used in this.

## Powerups implemented

### Long paddle 
### Short paddle 
### Thru Ball 
### Fast Ball
### Ball grab 
