class Sprite:
    sprite_count=0
    class Collider:
        def __init__(self, sprite, type="rectangle"):
            self.type = type
            self.width = sprite.width
            self.height = sprite.height
            self.scale = sprite.scale
            self.sprite_id = sprite.id
            self.parent = sprite
            
        def collide_sprite(self, sprite):
            if self.type == "circle":
                return (PVector.dist(self.parent.location, sprite.location) 
                            < (self.width * self.scale / 2 
                            + sprite.width * sprite.collider.scale / 2))
            else:     #rectangle
                return ((sprite.location.x - sprite.collider.width * sprite.collider.scale / 2 
                            < self.parent.location.x - self.width * self.scale / 2 
                            < sprite.location.x + sprite.collider.width * sprite.collider.scale / 2
                            or sprite.location.x - sprite.collider.width * sprite.collider.scale / 2
                            < self.parent.location.x + self.width * self.scale / 2
                            < sprite.location.x + sprite.collider.width * sprite.collider.scale / 2)
                            and (sprite.location.y - sprite.collider.height * sprite.collider.scale / 2 
                            < self.parent.location.y - self.height * self.scale / 2 
                            < sprite.location.y + sprite.collider.height * sprite.collider.scale / 2
                            or sprite.location.y - sprite.collider.height * sprite.collider.scale / 2
                            < self.parent.location.y + self.height * self.scale / 2
                            < sprite.location.y + sprite.collider.height * sprite.collider.scale / 2))
        

        def draw(self):
            stroke(0, 255, 0)
            fill(0, 255, 0)
            textAlign(CENTER)
            text(self.sprite_id, 0, -3)
            line(-5, 0, 5, 0)
            line(0, -5, 0, 5)
            noFill()
            if self.type == "circle":
                ellipse(0, 0, self.width * self.scale, self.width * self.scale)
            else:  # rectangle
                rect(-self.width/2*self.scale, -self.height/2*self.scale, 
                        self.width * self.scale, self.height * self.scale)

    def __init__(self, 
                location=None,
                velocity=None,
                width=20,
                height=20,
                scale=1):
        self.location = location or PVector(0,0)
        self.velocity = velocity or PVector(0,0)
        self.color = color(random(255), random(255), random(255))
        self.width = width
        self.height = height
        self.scale = scale
        self.gravity = PVector(0, 0)
        self.debug = False
        self.id = Sprite.sprite_count
        Sprite.sprite_count += 1
        self.collider = Sprite.Collider(self)
    
    def update(self):
        
        self.velocity.add(self.gravity)
        self.location.add(self.velocity)
        
        if self.location.x > width:
            self.location.x = width
            self.velocity.x *= -1
        elif self.location.x < 0:
            self.location.x = 0
            self.velocity.x *= -1
            
        if self.location.y > height:
            self.location.y = height
            self.velocity.y *= -1
        elif self.location.y < 0:
            self.location.y = 0
            self.velocity.y *= -1

        
    def draw(self):
        noStroke()
        fill(self.color)
        rect(self.location.x - self.width/2, self.location.y-self.height/2, self.width, self.height)
        if debug:
            pushMatrix()
            translate(self.location.x, self.location.y)
            self.collider.draw()
            popMatrix()
        
    def collide_point(self, point):
        """
        collide_point()
        @param PVector point
        @return Boolean
        """
        if self.collider.type == "circle":
            return (PVector.dist(self.location, point) 
                        < self.collider.width * self.collider.scale / 2)
        else:     #rectangle
            return 
        
    def collide_sprite(self, sprite):
        """
        collide_sprite()
        @param Sprite sprite
        @return Boolean
        """
        return self.collider.collide_sprite(sprite)
    
    def bounce(self, sprite):
        if self.collider.collide_sprite(sprite):
            sprite.velocity.add(self.velocity)
        
class Group(list):
    pass