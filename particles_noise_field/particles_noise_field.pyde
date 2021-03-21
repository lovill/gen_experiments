from flowfield import FlowField

TOFF = 0

def setup():

    size(400, 400)

    global flowfield

    flowfield = FlowField(scl=5)

def draw():

    background(220)
    global TOFF

    # flowfield.display_grid()
    flowfield.init_noise(zoff=TOFF)
    
    TOFF += 0.01
    flowfield.display_field()

    print(floor(frameRate))
