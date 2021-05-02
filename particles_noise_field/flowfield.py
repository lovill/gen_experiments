
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

    def grid_size(self):

        return (len(self._cells), len(self._cells[0]))

    def init_noise(self, noise_seed=0, zoff=0):
        """
        Assign perlin noise angle values to cells
        """
        noiseSeed(noise_seed)
        # inc = 0.0025
        # inc = 0.005
        # inc = 0.010
        inc = 0.025
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

    def display_curves(self, x, y, num_steps, max_steps=500):

        stroke_weight = 0.5
        hue = 240

        push()
        noFill()
        colorMode(HSB, 360, 100, 100)
        # stroke(
        #     map(num_steps, 0, 1000, 220, 270),
        #     map(num_steps, 0, 1000, 80, 100),
        #     100
        # )
        
        strokeWeight(stroke_weight)

        # beginShape()
        for n in range(num_steps):

            # curveVertex(x, y)
            stroke(
                hue,
                map(n, 0, max_steps, 0, 100),
                map(n, 0, max_steps, 0, 100)
            )
            circle(x, y, stroke_weight)

            x_offset = x 
            y_offset = y 

            column_index = int(x_offset / self._scl)
            row_index = int(y_offset / self._scl)

            #NOTE: normally you want to check the bounds here
            if column_index >= self.grid_size()[0]:
                column_index = self.grid_size()[0] - 1
                continue
            elif column_index <= - self.grid_size()[0]:
                column_index = - (self.grid_size()[0] - 1)
                continue

            if row_index >= self.grid_size()[1]:
                row_index = self.grid_size()[1] - 1
                continue
            elif row_index <= - self.grid_size()[1]:
                row_index = - (self.grid_size()[1] - 1)
                continue

            # print("grid size:{}".format(self.grid_size()))
            # print(column_index, row_index)

            grid_angle = self._cells[column_index][row_index]

            # step_length = width*0.0025
            step_length = width*0.001
            # step_length = width*0.00025

            x_step = step_length * cos(grid_angle)
            y_step = step_length * sin(grid_angle)
            x = x + x_step
            y = y + y_step
        
        # endShape()
        pop()

        colorMode(HSB, 360, 100, 100)
        # stroke(hue, 100, 100)
        stroke(
            hue,
            map(num_steps, 0, max_steps, 0, 100),
            map(num_steps, 0, max_steps, 0, 100)
        )   
        strokeWeight(2)
        circle(x, y, stroke_weight*1.25)


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
                    50
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


