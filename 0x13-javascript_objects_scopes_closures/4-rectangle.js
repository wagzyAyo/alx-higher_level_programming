#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0, y; x < this.height; x++) {
      y = '';
      for (let g = 0; g < this.width; g++) {
        y += 'X';
      }
      console.log(y);
    }
  }

  rotate () {
    const change = this.width;
    this.width = this.height;
    this.height = change;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
