class Ball:
    def __init__(self):
        self.pos = PVector(random(width), random(height))
        self.speed = PVector(random(-5, 5), random(-5, 5))
        self.color = color(random(200), random(200), random(200))
        self.size = random(10, 40)
        
    def draw(self, context=None):
        if not context:
            noStroke()
            fill(self.color)
            ellipse(self.pos.x, self.pos.y, self.size, self.size)
        else:
            context.noStroke()
            context.fill(self.color)
            context.ellipse(self.pos.x, self.pos.y, self.size, self.size)
        
    def update(self):
        self.pos.add(self.speed)
        if 0 > self.pos.x > width:
            self.speed.x *= -1
        if 0 > self.pos.y > height:
            self.speed.y *= -1
        self.pos.x = constrain(self.pos.x, 0, width)
        self.pos.y = constrain(self.pos.y, 0, height)
        

balls = []
rendered_frames = []

def setup():
    global rendered_frames, balls
    size(800, 800)
    
    # create and append balls
    for _ in range(10):
        balls.append(Ball())
    
    for _ in range(500):
        # update and draw balls to frame
        frame = createGraphics(width, height)
        frame.beginDraw()
        frame.background(255)
        for ball in balls:
            ball.update()
            ball.draw(frame)
        rendered_frames.append(frame)
        frame.endDraw()
    

def draw():
    global rendered_frames
    frameNumber = frameCount % len(rendered_frames)
    renderedFrameImage = rendered_frames[frameNumber]
    image(renderedFrameImage, 0, 0)
