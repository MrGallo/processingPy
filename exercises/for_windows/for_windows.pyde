# Windows on a high-rise
# Create a high-rise building with rect()
# use a for loop to draw windows in one column
# advanced: use a nested for loop to draw many columns
# advanced: Create a chess board in the same way

def setup():
    size(400, 400)
    
def draw():
    background(255)
    
    # building
    stroke(0)
    strokeWeight(5)
    fill(255)
    rect(125, 50, 150, 300)
    
    # window
    stroke(0)
    strokeWeight(2)
    fill(128)
    
    # place the following line in a for loop to 
    # draw multiple rects in a column
    rect(135, 63, 30, 40)