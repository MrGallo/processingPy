"""
Create a 2-player clicking game.

1. Draw an ellipse at a random location on the screen. Be sure to
   store the location info in x/y position variables (or PVector?)
2. Define a mousePressed() function. When the user clicks,
   assign a new location to the ball.
3. Create a score variable. When the user clicks (same function above,
   add +1 to the score.
4. Display the score using the text() function.
   https://processing.org/reference/text_.html
5. Now, when the user clicks, use the mouseX and mouseY variables, within the
   previously defined mousePressed() function, compare those values to the 
   location of the ellipse. 
   If the mouse location is within a certain range, then you add to the 
   score and change the ellipse location.
6. Split the board visually in the middle. One side will be for player 1, the
   other for player2. Each will have their own ball to click...
7. Add a second ball, with its own position variable, and its own score, and
   its own click detection in the already defined mousePressed() function.
8. If a player reaches a score of 10, they win. Code this.
"""

pos_x = 0
pos_y = 0

def setup():
    global pos_x
    global pos_y
           
    size(800, 400)
    pos_x = random(0, width)
    pos_y = random(0, height)


def draw():
    background(0)
    ellipse(pos_x, pos_y, 40, 40)
    

def mousePressed():
    global pos_x
    global pos_y
    pos_x = random(0, width)
    pos_y = random(0, height)
