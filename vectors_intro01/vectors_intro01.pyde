# Vectors!!!!
# 1. Create variables for a ball that moves 
# You need a x-position, x-position
# also a x-speed and y-speed variable
# no need for a draw loop for now.

x = 50
y = 50
xSpeed = 10
ySpeed = 0

def setup():
    frameRate(1)
    size(600, 600)
    background(255)
    
def draw():
    global x
    global y
    global xSpeed
    global ySpeed
    
    x += xSpeed
    
    background(255)
    ellipse(x, y, 30, 30)
