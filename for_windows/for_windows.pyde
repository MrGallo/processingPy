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
    for y in range(63, 303, 47):
        rect(135, y, 30, 40)
        