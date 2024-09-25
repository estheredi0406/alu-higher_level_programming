#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        this.width = w;  // Initialize the instance attribute width
        this.height = h; // Initialize the instance attribute height
    }
}

// Example usage:
const r1 = new Rectangle(5, 10); // Create a new rectnagle instance with width 5 and height 10
console.log(r1); // Output: Rectangle { width: 5, height: 10 }
