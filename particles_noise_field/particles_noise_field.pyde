from flowfield import FlowField

TOFF = 0.05

def setup():

    size(600, 600)
    # blendMode(BLEND)
    global flowfield

    flowfield = FlowField(scl=10)


def draw():

    colorMode(HSB, 360, 100, 100)
    background(0)
    global TOFF

    # flowfield.display_grid()
    flowfield.init_noise(zoff=TOFF)
    
    # TOFF += map(mouseY, 0, height, 0.01, 0.5)
    TOFF += 0.001
    # flowfield.display_field()

    y_steps = 70
    x_steps = 70
    max_steps = 500
    for i in range(y_steps):
        y_step = i / float(y_steps)

        for j in range(x_steps):

            x_step = j / float(x_steps)

            # num_steps = int(map(y_step * x_step, 0, 1, 50, 800))
            # num_steps = int(noise(x_step, y_step) * max_steps)
            num_steps = int(random(0, 1) * max_steps)

            flowfield.display_curves(width * x_step, height * y_step, num_steps, max_steps)

    # n = 200
    # for k in range(n):

    #     x = cos((k/float(n)) * PI)*300 + width/2
    #     y = sin((k/float(n)) * PI)*100 + 600

    #     fill(0)
    #     # circle(x, y, 2)

    #     # num_steps = int(random(0, 1) * 1000)
    #     num_steps = int(noise(x, y) * 6000)
    #     flowfield.display_curves(x, y, num_steps)
    
    noLoop()

    # print(floor(frameRate))
