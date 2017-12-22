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
    friction = 1
    def __init__(self):
        self.pos = PVector(random(width), random(height))
        self.speed = PVector(random(-5, 5), random(-5, 5))
        self.color = color(random(240), random(240), random(240))
        self.width = 30
        self.height = self.width
        self.mass = 1
        
    
    def collide(self, others):
        for other in others:
            diff = PVector.sub(self.pos, other.pos)
            distance = diff.mag()
            angle = diff.heading()
            # assuming circular sprites
            if distance < other.width/2 + self.width/2:
                v_x1 = (self.speed.x * (self.mass - other.mass) + (2.0 * other.mass * other.speed.x)) / (self.mass + other.mass)
                v_y1 = (self.speed.y * (self.mass - other.mass) + (2.0 * other.mass * other.speed.y)) / (self.mass + other.mass)
                
                v_x2 = (other.speed.x * (other.mass - self.mass) + (2.0 * self.mass * self.speed.x)) / (other.mass + self.mass)
                v_y2 = (other.speed.y * (other.mass - self.mass) + (2.0 * self.mass * self.speed.y)) / (other.mass + self.mass)

                self.speed.set(v_x1, v_y1)
                other.speed.set(v_x2, v_y2)
                
                print(self.speed)
                print(other.speed)
                
                noLoop()
                
    
    def update(self):
        self.speed.mult(Sprite.friction)
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
    # for _ in range(20):
    #     sprites.append(Sprite())   
    
    sp1 = Sprite()
    sp1.pos.set(200, height/2)
    sp1.speed.set(1, 0)
    
    sp2 = Sprite()
    sp2.pos.set(250, height/2)
    sp2.speed.set(-1, 0.4)
    
    sprites.append(sp1)
    sprites.append(sp2)
    
    
def draw():
    time = millis()
    background(255)
    for i, sprite in enumerate(sprites):
        sprite.update()
        # Collide check with remaining sprites.
        sprite.collide(sprites[i+1:])
        sprite.draw()
    #print("ms: " + str(millis() - time)) 
    
    
def mousePressed():
    loop()