# Weird player movement fix
# Problem: When you move a sprite with the keyboard, and you hold
# multiple keys, there is a stuttering motion, or an unintuitive motion.
# The keyCode variable will hold only one value at a time. A problem when
# we need to account for multiple keys.
#
# Solution: create a list that stores the state of each key 
# Use this list to check if a key is being held.
# Each key has a keyCode number.
# This will be the key's index value in the list.
# Using the keyPressed() function, we set the list at that keycode
# index to True.
# Using the keyReleased() function, we set the keycode index to False.


key_states = []
# pre-populate the list. There are about 222 possible keycodes.
# There is a cooler way to do this. Look at list comprehensions.
# This method is the most understandable for the beginner.
for _ in range(223):
    key_states.append(False)

player = PVector(50, 50)

def setup():
    size(400, 400)
    
    
def draw():
    # Key codes for arrows are:
    # left: 37
    # up: 38
    # right: 39
    # down: 40
    
    if key_states[37]:  # left
        player.x -= 3
    elif key_states[39]:  # right
        player.x += 3
        
    if key_states[38]:  # up
        player.y -= 3
    elif key_states[40]:  # down
        player.y += 3
    
    background(255)
    fill(0)
    ellipse(player.x, player.y, 30, 30)
    

def keyPressed():
    global key_states
    key_states[keyCode] = True
    
    
def keyReleased():
    global key_states
    key_states[keyCode] = False