# Define and initialize GLOBAL variables
x = 100
speed = 1

def setup():
    size(400, 400)
    
def draw():
    # Pull in global variables
    global x  
    global speed

    x += speed  # change location
    
    # Boundary collisions
    # When the ball hits a boundary,
    # change its direction by 
    # inverting its speed.
    if x >= 400:
        speed = -speed
    elif x <= 0:
        speed = -speed
        
    # DRAWING
    background(255)
    noStroke()
    fill(0, 100, 0)
    ellipse(x, 100, 40, 40)
