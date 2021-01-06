
let N = 20, Niter = 5; ampl_x = 300; ampl_y = 100;

function setup() {
    createCanvas(600, 600);
    background(0);
    blendMode(ADD);

    for (let n=0; n<N; n++) {
        for (let i=0; i<Niter; i++) {
            theta = 0.0;

            while (theta < TWO_PI) {
                th_offset = random(-1, 1);

                stroke(255, random(50));
                strokeWeight(random(5));

                // point(width/2 + ampl_x*cos(theta+th_offset),
                //     height/2 + ampl_y*sin(theta)
                //     );

                point(
                    width/2,
                    height/2
                    );

                theta += 0.2;
            }

        }
    }
}

function draw() {

}