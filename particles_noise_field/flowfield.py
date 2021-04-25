
NOISE_PI = 4*TWO_PI

class FlowField(object):

    def __init__(self, scl):

        # size of grid cell
        self._scl = scl

        # get number of cols and rows
        self._cols = floor(width / scl)
        self._rows = floor(height / scl)
        self._cells = self.init_2darray()
        # self.init_noise()

    def init_2darray(self):

        arr = []

        for x in range(self._cols):
            arr.append([])

            for y in range(self._rows): 
                arr[x].append(None)

        return arr

    def init_noise(self, noise_seed=1, zoff=0):
        """
        Assign perlin noise angle values to cells
        """
        # noiseSeed(noise_seed)
        inc = 0.008
        # inc = 0.05
        # inc = map(mouseX, 0, width, 0.001, 0.5)
        yoff = 0

        for y in range(self._rows):

            xoff = 0

            for x in range(self._cols):

                noise_theta = noise(xoff, yoff, zoff) * NOISE_PI

                self._cells[x][y] = noise_theta

                xoff += inc

            yoff += inc

        # zoff += inc


    def display_grid(self):

        for y in range(self._rows):

            for x in range(self._cols):

                noFill()
                stroke(0)
                rect(
                    x * self._scl, 
                    y * self._scl, 
                    self._scl, 
                    self._scl
                )

    def display_field(self):

        for y in range(self._rows):

            for x in range(self._cols):

                theta = self._cells[x][y]

                # print((mouseY/height)*255)

                push()
                stroke(
                    map(theta, 0, NOISE_PI, 0, 10),
                    map(theta, 0, NOISE_PI, 0, 255),                    
                    map(theta, 0, NOISE_PI, 255, 0),
                    255
                )

                noFill()
                strokeWeight(1)
                translate(x * self._scl, y * self._scl)
                rotate(theta)
                strokeCap(ROUND);
                line(0, 0, self._scl, 0)
                # circle(0, 0, self._scl)
                pop()


    def display_2d_perlinnoise(self):

        inc = 0.05
        yoff = 0

        for y in range(self._rows):

            xoff = 0
            for x in range(self._cols):

                noise_val = noise(xoff, yoff) * 255

                fill(noise_val)
                noStroke()
                rect(
                    x * self._scl, 
                    y * self._scl, 
                    self._scl, 
                    self._scl
                )

                xoff += inc
            yoff += inc


