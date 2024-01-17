class Shape {
    constructor(width, height, color) {
        this.width = width;
        this.height = height;
        this.color = color;
    }

    draw() {
        console.log(`drawing this shape!`);
    }

    getArea() {
        const area = this.width * this.height
        console.log(`area is ${area}`);
    }
}

class Rectangle extends Shape {}
class Triangle extends Shape {
    getArea() {
        const area = this.width * this.height * 0.5
        console.log(`area is ${area}`);
    }   
}

const rec = new Rectangle(10, 20, 'blue');
rec.draw();
rec.getArea();

const tri = new Triangle(10, 20, 'red');
tri.getArea();