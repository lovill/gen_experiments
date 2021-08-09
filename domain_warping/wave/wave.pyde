f_mult = 0

def setup():

    size(1200, 500)
    background(255)

def draw():

    background(255)

    n_points = 100
    verts = []
    for x in range(n_points):

        x_spacing = width/n_points
        x *= x_spacing

        # WAVE FUNCTION
        amplitude = 100.
        frequency = map(f_mult, 0, width, 0., 0.5)
        y = wave(x=x, amplitude=amplitude, frequency=frequency)

        display_frequency(frequency)

        verts.append((x, y))

    draw_wave(verts)

    global f_mult
    f_mult += 1.


###FUNCTIONS

def wave(x, amplitude, frequency):
    y = amplitude * sin(x * frequency)
    return y

def display_frequency(f):

    s = "frequency: {}".format(f)
    fill(50)
    textSize(10)
    text(s, 10, 10, 200, 80) 

def draw_wave(verts):

    noFill()
    strokeWeight(2)
    beginShape()
    for v in verts:
        curveVertex(v[0], v[1] + height/2)
    endShape()