t = 0

def setup():

    size(1200, 500)
    background(255)

def draw():

    background(255)

    n_points = 1100
    verts = []
    for x in range(n_points):

        x_spacing = width/n_points
        x *= x_spacing

        # WAVE FUNCTION
        amplitude = 5.
        frequency = 0.01

        y = wave(
            x = x,
            amplitude=amplitude,
            frequency=frequency
        )

        y += wave(
            x=x, 
            amplitude=amplitude, 
            frequency=frequency,
            f_mult=2.5,
            t=t,
            k=3
        )

        y += wave(
            x=x, 
            amplitude=amplitude, 
            frequency=frequency,
            f_mult=1.2,
            t=t,
            t_mult=0.24,
            k=4.2
        )

        y += wave(
            x=x, 
            amplitude=amplitude, 
            frequency=frequency,
            f_mult=4.0,
            t=t,
            t_mult=0.002,
            k=map(mouseX, 0, width, 0, 5.)
        )

        y *= amplitude*0.6

        display_frequency(frequency)
        verts.append((x, y))

    draw_wave(verts)

    global t
    t += second()*0.0025
    print(t)
    if t >= 1000:
        t *= -1

###FUNCTIONS

def wave(x, amplitude, frequency, f_mult=1, t=0, t_mult=1, k=1):
    y = amplitude * sin(x*frequency*f_mult + t*t_mult) * k
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

    strokeWeight(10)
    stroke(0)
    point(verts[-1][0], verts[-1][1] + height/2)
