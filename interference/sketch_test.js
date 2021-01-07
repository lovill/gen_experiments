let THETA = 0., n_points = 4000, ampl_y = 100, ampl_x = 250;
let X = 0;
let X_OFFSET = 0., Y_OFFSET = 0.;

// Increase difference between min and max to control blur effect.
// Both can be 0.
let rand_offs_x_min = -20, rand_offs_x_max = 0;
// high sensitivity for form. Start from same number and change decimal points.
let th_mult_x = 2, th_mult_y = 1.85;
// increase difference to change phase offset.
let th_offset_min = -5, th_offset_max = 0.1;

function setup() {
    createCanvas(600, 600);
}

function draw() {
    background(0);
    blendMode(ADD);

    for (let i=0; i<n_points; i++) {

        let rand_offset_x = random(rand_offs_x_min, rand_offs_x_max);
        let rand_offset_y = random(-0.5, 1);
        let th_offset = random(th_offset_min, th_offset_max);

        let x_coord = (ampl_x+rand_offset_x)*cos(THETA+th_offset*th_mult_x);
        let y_coord = (ampl_y+Y_OFFSET)*tan(THETA+th_offset*th_mult_y);

        stroke(
            // map(x_coord, -ampl_x, ampl_x, 255, 0),
            map(THETA, 0, 5*TWO_PI, 255, 0),
            map(THETA, 0, 5*TWO_PI, 50, 255),
            // map(y_coord, -ampl_x, ampl_x, 50, 255),
            map(THETA, 0, 5*TWO_PI, 0, 255),
            random(25));
        strokeWeight(random(3));
        push();
        translate(width/2, height/2);
        point(x_coord, y_coord);
        pop();
    }
    X_OFFSET += random(-0.5, 1);
    Y_OFFSET += random(-1, 2);
    X += 1.;
    THETA += 0.1;
    if (THETA>5*TWO_PI) {
        noLoop();
    }

    // save("test" + frameCount + ".jpg");
    // if (frameCount > 100) {
    //     noLoop();
    // }

}

function keyTyped() {
    if (key == 's') {
        save('dots.png')
        return false;
    }
}