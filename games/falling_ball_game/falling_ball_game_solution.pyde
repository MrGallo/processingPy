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
ball_1_pos_x = 0
ball_1_pos_y = 0
ball_1_speed_x = 0
ball_1_speed_y = 3  # moving 3 pixels per frame
ball_1_size = 40

player_pos_x = 0
player_pos_y = 0
player_size = 40

background_color = color(39, 76, 119)
primary_color = color(96, 150, 186)
secondary_color = color(163, 206, 241)

score = 0

def setup():
    size(400, 600)
    
def draw():
    global ball_1_pos_x
    global ball_1_pos_y
    global ball_1_speed_x
    global ball_1_speed_y
    global score
    
    # Update ball 1's location
    ball_1_pos_y += ball_1_speed_y
    
    # Update player position based on mouse
    player_pos_x = mouseX
    player_pos_y = height - player_size/2
    
    if ball_1_pos_y > height:
        ball_1_pos_y = 0
        ball_1_pos_x = random(0, width)
        score += 1
    
    # Collision detection.
    # Using pythagorean theroem
    radius_ball_1 = ball_1_size/2
    radius_player = player_size/2
    a = ball_1_pos_x - player_pos_x
    b = ball_1_pos_y - player_pos_y
    distance = sqrt(a**2 + b**2)  # hypotenuse of the R-A triangle
    if distance <= radius_ball_1 + radius_player:
        score = 0
        ball_1_pos_y = 0
        ball_1_pos_x = random(0, width)
        
    background(background_color)  # Remove streaking
    
    #Draw ball 1
    noStroke()
    fill(secondary_color)
    ellipse(ball_1_pos_x, ball_1_pos_y, ball_1_size, ball_1_size)
    
    # Draw score
    fill(primary_color)
    textSize(40)
    textAlign(LEFT)
    text(score, 20, 50)
    
    # Draw Player
    fill(primary_color)
    ellipse(player_pos_x, player_pos_y, player_size, player_size)
