
def setup():
    size(800, 900)

def draw():
    background(255)

    num_pts = 200
    verts = []
    for x in range(num_pts):

        octaves = int(map(mouseX, 0, width, 1, 12))
        print(octaves)

        x_spacing = (width + width*0.25)/num_pts
        x *= x_spacing
        y = fbm(
            x=x, 
            octaves=2, 
            ampl=0.5
        )

        verts.append([x, y])

    draw_wave(verts, k=200)

def fbm(x, ampl=0.5, f=1., octaves=1, l=2., g=0.5):

    # Properties
    octaves = 24
    lacunarity = l
    gain = g
    y = 0
    
    # Initial values
    amplitude = ampl
    frequency = f
    
    # Loop of octaves
    for i in range(octaves):
        y += amplitude * noise(frequency*x)
        frequency *= lacunarity
        amplitude *= gain

    return y


def draw_wave(verts, k=1):

    noFill()
    strokeWeight(2)
    beginShape()
    for v in verts:
        curveVertex(v[0], v[1]*k + height/2)
    endShape()

    strokeWeight(10)
    stroke(0)
    point(verts[-1][0], verts[-1][1] + height/2)
    
