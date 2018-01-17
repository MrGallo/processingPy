# lerpColor() gradient
# The idea is to use a loop to draw horizontal (or vertical) lines
# Each line moving gradually closer to the destination color.
# You can stretch the gradient with some math.

def setup():
    size(400, 400)
    
def draw():
    background(255)
    
    beginning = color(204, 102, 0)
    ending = color(0, 102, 153)
    
    for i in range(101):
        stroke(lerpColor(beginning, ending, i/100.0))
        line(0, i, width, i)
    