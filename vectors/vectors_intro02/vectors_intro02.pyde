# Vectors!!!!
# 1. Create variables for a ball that moves 
# You need a x-position, x-position
# also a x-speed and y-speed variable
# no need for a draw loop for now.
#
# 2. Convert the variables to PVector objects. 
#    Objects have:
#      attributes - info for specific object (i.e., location)
#      behaviours - things they can DO (methods like .add())
#
# 3. Get the ball to bounce along the border.
 
pos = PVector(50, 50)
speed = PVector(3, 0)

def setup():
    frameRate(60)
    size(600, 600)
    background(255)
    
def draw():
    global pos
    global speed
    
    pos.add(speed)
    
    background(255)
    ellipse(pos.x, pos.y, 30, 30)