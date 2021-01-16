let x = 0;
let y = 0

function setup() {
	createCanvas(800, 800);
}


function draw() {
	background(0);
	blendMode(ADD);

	stroke(255, random(25));
	strokeWeight(random(3));

	translate(width/2, height/2);
	point(x, y)

	x += 0.1
	y += 0.1
}