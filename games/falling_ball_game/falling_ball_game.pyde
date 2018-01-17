"""
Create a dodging game.
Ellipses will start at the top of the screen and 
fall downwards. 

The Player controls the movement of an ellipse 
at the bottom of the screen using the mouse.

The player must dodge the falling ball

Steps:
    1. Create an ellipse with its own 
    position variables. Draw it in the draw() function
    This will be the falling ball.
    2. Make this ball "fall" by giving it a y-speed.
    Update its location in the draw() function.
    Also give it an x-speed, but keep it at 0
    (unless you want to mess around a bit).
    3. When the ball hits the bottom of the screen,
    reset its position to the top of the window.
    You can assign the x-position to a random value.
    Maybe even assign the y-speed to a random value 
    as well. Also, possibly create a second falling 
    ball.
    4. Create the PLAYER ellipse with its own position
    variables. The position of the PLAYER will update
    every draw loop. In the draw loop, bind the 
    x-location variable to the mouseX variable.
    Keep this ball at the bottom of the screen. 
    Draw this ball in the draw() function.
    This will be the player.
    5. Whenever the ball hits the bottom, add +1 to a score
    variable. Draw this score with the text() function.
    6. In the draw() function determine if the two
    ellipses are touching:
        a) Use pythagorean theorem to find out the 
        distance (hypotenuse) between the two origins.
        b) check to see if the distance is less than 
        the two ellipse radii. (Radiuses)
    7. Whenever the falling ellipses touch the player, 
    reset the score.
"""

def setup():
    size(400, 600)
    
def draw():
    ellipse(50, 50, 20, 20)
