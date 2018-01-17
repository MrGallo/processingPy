def setup():
    size(400, 400)

def draw():
    background(255)
    noStroke()
    
    # face
    fill(255, 255, 0)
    ellipse(200, 200, 300, 350)
    
    # left eye
    fill(255)
    ellipse(150, 150, 75, 100)
    # iris
    fill(0)
    ellipse(165, 160, 30, 30)
    
    # right eye
    fill(255)
    ellipse(250, 150, 75, 100)
    # iris
    fill(0)
    ellipse(240, 130, 30, 30)
    
    #mouth
    fill(0)
    ellipse(200, 270, 60, 90)
    
    