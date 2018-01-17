"""
TO have a menu, screen, instructions, play, or any other screen, simply 
create a variable that 'remembers' what screen to display so the draw()
function can check what screen it is with an if statement. This screen
variable can be a number or string, whatever you want.  I use a string 
in this example to make it easier to read.
"""

screen = "menu"

def setup():
    size(400, 400)
    
    
    
def draw():
    global screen
    if screen == "menu":
        if keyPressed:
            if key == "i":
                screen = "instructions"
        
        background(0)
        fill(255)
        textSize(30)
        textAlign(CENTER)
        text("Menu Screen", width/2, height/2)
        textSize(14)
        text("press [i] for instructions", width/2, height/2 + 30)
    elif screen == "instructions":
        if keyPressed:
            if key == "m":
                screen = "menu"
            
        background(255, 255, 255)
        fill(0)
        textSize(30)
        textAlign(CENTER)
        text("Instructions Screen", width/2, height/2)
        textSize(14)
        text("press [m] to go back", width/2, height/2 + 30)
