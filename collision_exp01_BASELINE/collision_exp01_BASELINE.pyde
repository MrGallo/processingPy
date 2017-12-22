"""
BASELINE
Experiment to find efficient collision detection
3D List

Screen divided into a grid with a 2D list.
Sprites only within a given cell will be
checked for collision.

Sprites between cells will belong potentially to all (two/four) cells
it intersects with.

Only when the sprites move will they be assigned their cell.
"""


class Sprite():
    def __init__(self):
        self.pos = PVector(random(width), random(height))
        self.speed = PVector(random(-5, 5), random(-5, 5))
        self.color = color(random(240), random(240), random(240))
        self.width = 30
        self.height = self.width
        self.mass = 1
    
    def update(self):
        self.pos.add(self.speed)
        
        if self.pos.x > width or self.pos.x < 0:
            self.speed.x *= -1
            self.pos.x = constrain(self.pos.x, 0, width)
        if self.pos.y > height or self.pos.y < 0:
            self.speed.y *= -1
            self.pos.y = constrain(self.pos.y, 0, height)
        
        
        
    def draw(self):
        noStroke()
        fill(self.color)
        ellipse(self.pos.x, self.pos.y, self.width, self.height)
        
        
sprites = []     

def setup():
    size(800, 800)
    for _ in range(4):
        sprites.append(Sprite())   
    
def draw():
    time = millis()
    background(255)
    for sprite in sprites:
        sprite.update()
        sprite.draw()
    print("ms: " + str(millis() - time)) 