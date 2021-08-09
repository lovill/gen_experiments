
def setup():

    print(hour(), minute())

    size(400, 400)
    # background(255)

    increment = 0.02

    loadPixels()

    xoff = 0.
    for ix in range(width):
        xoff += increment
        yoff = 0.

        for iy in range(height):
            yoff += increment
            z = fbm_2d(x=xoff, y=yoff)
            pix_id = get_pixel_id(ix, iy)

            pixels[pix_id] = color(0,0,0,z*255)

    updatePixels()

    print(hour(), minute())



def fbm_2d(x, y, ampl=0.5, f=1., octaves=1, l=2., g=0.5):

    # Properties
    octaves = 24
    lacunarity = l
    gain = g
    z = 0
    
    # Initial values
    amplitude = ampl
    frequency = f
    
    # Loop of octaves
    for i in range(octaves):
        noiseSeed(1)
        z += amplitude * noise(x, y)
        frequency *= lacunarity
        amplitude *= gain

    return z

def get_pixel_id(x, y):
    return (x + y * width)