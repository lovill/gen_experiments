theta = 0.
n_points = 8000

ampl_x = 250
ampl_y = 250
ampl_offs_x = 0
ampl_offs_y = 0
#Increase difference between min and max to control blur effect.
#both can be 0.
rand_ampl_offs_x_min = -20
rand_ampl_offs_x_max = 20

#increase difference to change phase offset.
th_offset_min = -5
th_offset_max = 5

#high sensitivity for form. Start from same number and change decimal points.
th_offs_mult_x = 50
th_offs_mult_y = 20

recording = False
frame_h = hour()
frame_s = second()

def setup():
    theta = 0
    size(900, 900)
    background(0)

def draw():


    global theta, ampl_offs_x, ampl_offs_y

    for _ in range(n_points):

        rand_ampl_offs_x = random(rand_ampl_offs_x_min, rand_ampl_offs_x_max)
        th_offset = random(th_offset_min, th_offset_max)

        x = (ampl_x + rand_ampl_offs_x) * cos(theta + th_offset * th_offs_mult_x)
        y = (ampl_y + ampl_offs_y) * sin(theta + th_offset * th_offs_mult_y)

        push()
        blendMode(ADD)
        stroke(255, random(25))
        stroke(
            map(x, -ampl_x, ampl_x, 255, 0),
            # map(theta, 0, 5*TWO_PI, 255, 0),
            # 255,
            map(theta, 0, 5*TWO_PI, 100, 0),
            # map(y, -ampl_x, ampl_x, 50, 255),
            map(theta, 0, 5*TWO_PI, 50, 255),
            random(25)
        )
        strokeWeight(random(3))

        translate(width/2, height/2)
        point(x, y)
        pop()
        # th_offset += random(1, 1.5)

    theta += 0.1;
    ampl_offs_x += random(-0.5, 1)
    ampl_offs_y += random(-1, 2)


    ##### RECORDING
    record_frames()
    ##### RECORDING

    if (theta > 5*TWO_PI):
        noLoop()
        save('output/interference_{}_{}{}.png'.format(frameCount, hour(), second()))
        print('done.')

def keyPressed():
    global recording
    if (key == 'r' or key == 'R'):
        recording = not recording

def record_frames():
    if recording:
        saveFrame("output/frames_{}{}/interference_#####.png".format(
            frame_h, frame_s))
    #     fill(255, 0, 0)
    # else:
    #     fill(0, 255, 0)
    # ellipse(width/2, height*0.9, 20, 20)
