# Python translation of lerpColor()
# https://processing.org/reference/lerpColor_.html
# lerpColor() calculates a color between two colors at a specific increment.

def setup():
    size(400, 400)
    
def draw():
    stroke(255)
    background(51)
    
    beginning = color(204, 102, 0)
    ending = color(0, 102, 153)
    between1 = lerpColor(beginning, ending, .33)
    between2 = lerpColor(beginning, ending, .66)
    
    fill(beginning)
    rect(10, 20, 20, 60)
    
    fill(between1)
    rect(30, 20, 20, 60)
    
    fill(between2)
    rect(50, 20, 20, 60)
    
    fill(ending)
    rect(70, 20, 20, 60)