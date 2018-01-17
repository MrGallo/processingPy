# Create an image within processing.
# This is useful when you want to randomly generate
# certain things and have the computer "remember" the image.
# Also, you can draw an entire character to an image and 
# when you move the character, all you have to do is draw the whole
# image in a different place, rather than coupling every shape to the
# location variable.

# Declare a variable to hold the image
img = None

def setup():
    size(400, 400)
    
    # Create my static image
    global img
    img = createGraphics(width/4, height/4)
    img.beginDraw()
    img.background(0)
    img.fill(255, 0, 0)
    
    # create 200 circles, randomly dispersed
    for i in range(200):
        x = random(img.width)
        y = random(img.height)
        diameter = random(5, 15)
        img.ellipse(x, y, diameter, diameter)
    img.endDraw()

def draw():
    global img
    background(255)
    image(img, 50, 50)  # draw the image