# Enter text into your sketch
# Have a global variable to store a string, which you will
# add each character to each time a key is pressed.
# Thus, you will need to make use of the keyPressed() function.

# Global variables
input_text = ""

def setup():
    size(400, 400)
    
    
    
def draw():
    background(255)
    
    textSize(20)
    
    # Input label (prompt)
    fill(0)
    text("Enter text:", 50, height/2)
    
    # Disply global string
    fill(255, 0, 0)
    text(input_text, 155, height/2)
    
    
    
def keyPressed():
    global input_text
    
    if key == BACKSPACE:
        # Remove the last character from the input_string
        print("Pressed Backspace")
    elif key == ENTER:
        # Submit reaponse
        print("Pressed Enter")
    else:
        # Add character to input_string
        input_text = input_text + key