from sprite import Sprite


sprites = []
player = None
def setup():
    global player
    size(800, 600)
    frameRate(60)
    
    player = Sprite()
    player.velocity = PVector(1, 0)
    player.location = PVector(30, 30)
    sprites.append(player)
    for _ in range(30):
        sp = Sprite(width=random(20, 40), height=random(20,40))
        sp.location = PVector(random(width), random(height))
        # sp.collider.scale = random(0.2, 3)
        # sp.velocity = PVector(random(-5, 5), random(-5, 5))
        # sp.gravity = PVector(0, 0.3)
        sp.debug = True
        sprites.append(sp)
    
def draw():
    background(0)
    player.velocity.rotate(map(noise(0), 0, 1, -0.05, 0.05))
    for sp in sprites:
        sp.update()
        sp.draw()
        player.bounce(sp)