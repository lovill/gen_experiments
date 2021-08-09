def setup():
    size(100, 100)
    background(255)
    pixelDensity(1)

def draw():

    loadPixels()

    for ix in range(width):
        for iy in range(height):
            pix_id = get_pixel_id(ix, iy)
            pixels[pix_id] = color(255,0,0)

    updatePixels()


def get_pixel_id(x, y):
    return (x + y * width)