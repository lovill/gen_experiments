
let nx = 600;
let offs_mult = 6;
let p2_n = 100;
let y;
let op_fall_rate = 20;

function setup() {
    createCanvas(600, 600);

}

function draw() {
    background(0);
    blendMode(ADD);

    let op = 255;

    for (let iter_=0; iter_<4; iter_++) {

        y = random(0, height);
        let noise_mult = random(0.005, 0.015)
        // console.log(y);

        for (let i=0; i<nx; i++) {
            let x = map(i, 0, nx, 0, width);
            noiseSeed(y);
            let n = noise(x*noise_mult);
            push();
            stroke(255, 255);
            strokeWeight(1.5);
            // point(x, y*n);
            pop();

            let offs = 0;
            for (let p2=0; p2<p2_n; p2++) {

                push();
                stroke(255, op*map(p2, 0, p2_n*0.75, 1, 0));
                strokeWeight(random(2)*map(p2, 0, p2_n, 1, 0.01));
                // translate(x, y*n);
                point(x, y*n+offs*offs_mult);
                pop();

                offs += noise(x*0.1, p2*0.1);
            }
        }

        op -= random(op_fall_rate);
    }
    noLoop();
}

function keyTyped() {
    if (key == 's') {
        save('dots.png')
        return false;
    }
}
