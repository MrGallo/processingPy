# An explanation of the various mouse events
"""
Mouse Variables and Functions

mouseButton
    -Variable that holds which mouse button is pressed.
mouseClicked()
    - ** Used outside of draw() function.
    - A click is an down and up motion. Will trigger on button RELEASE.
mouseDragged()
    - ** Used outside of draw() function.
    - Will trigger when a mouse button is down AND the mouse is moved.
mouseMoved()
mousePressed()
    - **Used outside of the draw() function.
    - Triggers as soon as a button is pressed down.
    - Will only trigger once, even if you hold the button.
mousePressed
    - Used in draw() function.
    - True if a button is currently being pressed, False otherwise.
    - Used if you need to continuously hold the button.
mouseReleased()
    - ** Used outside the draw() function
mouseWheel(event)
    - ** Used outside the draw() function.
    - Triggers ech notch of a wheel turn.
    - Requires an event parameter. The event variable will contain info
    about the mouse event.
mouseX
    - Current mouse x location
mouseY
    - Current mouse y location
pmouseX
    - Previous mouse x location. (previous frame)
pmouseY
    - Previous mouse y location. (previous frame)
"""

rectX = 50
rectY = 50
rectSize = 10

ballSize = 10

def setup():
    size(400, 400)
    
# Move the mouse quickly to see the difference 
# between the current and previous position 

def draw():
    background(255)
    
    if mousePressed:
        #Change background based on what mouse button is pressed
        if mouseButton == LEFT:
            background(255, 0, 0)
        elif mouseButton == CENTER:
            background(0, 255, 0)
        elif mouseButton == RIGHT:
            background(0, 0, 255)
    
    fill(0)
    rect(rectX, rectY, rectSize, rectSize)
    
    fill(255, 0, 0)
    ellipse(200, 200, ballSize, ballSize)
    
    if not mousePressed:
        fill(0, 255, 0)
        ellipse(mouseX, mouseY, mouseX, mouseY)
    

def mouseClicked():
    # A "Click" is a down+up motion, triggered on the up.
    # When a click occurs, assign a random size to the red ball
    global ballSize
    ballSize = random(5, 200)


def mouseDragged():
    # Adjust the rectangles size based on how fast you move the mouse.
    # Makes use of pmouseX which is where the mouse was previously.
    # The difference between the previous location and the current determines the size.
    global rectSize 
    rectSize = (pmouseX - mouseX) * 10
    
    
def mouseMoved():
    print("Mouse moved at frame # " + str(frameCount))
    
    
def mousePressed():
    print("Mouse pressed at frame # " + str(frameCount))
    

def mouseWheel(event):
    # event.count gives you the direction, 1 or -1
    # other useful attributes are:
    # .x, .y (mouse location)
    # .altDown, .shiftDown, .controlDown (True if any of those keys are pressed while scrolling)
    
    print("Mouse wheel: " + str(event.count))