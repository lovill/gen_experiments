from flowfield import FlowField

TOFF = 0.05

def setup():

    size(400, 400)
    # blendMode(BLEND)
    global flowfield

    flowfield = FlowField(scl=5)

def draw():

    background(220)
    global TOFF

    # flowfield.display_grid()
    flowfield.init_noise(zoff=TOFF)
    
    # TOFF += map(mouseY, 0, height, 0.01, 0.5)
    # TOFF += 0.001
    flowfield.display_field()

    print(floor(frameRate))
