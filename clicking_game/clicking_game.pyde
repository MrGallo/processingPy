"""
Create a 2-player clicking game.

1. Draw an ellipse at a random location on the screen.
2. Store the location info in a variable (PVector?)
3. Using the mousePressed() function. When the user clicks,
   assign a new location to the ball.
4. Create a score variable. When the user clicks (same function above,
   add +1 to the score.
5. Display the score using the text() function.
   https://processing.org/reference/text_.html
6. Now, when the user clicks, use the mouseX and mouseY variables, within the
   mousePressed() function, compare those values to the location of the ellipse. 
   If the mouse location is within a certain range, then you add to the 
   score and change the ellipse location.
7. Add a second ball, with its own position variable, and its own score, and
   its own click detection in the mousePressed() function.
8. If a player reaches a score of 10, they win. Code this.
"""
