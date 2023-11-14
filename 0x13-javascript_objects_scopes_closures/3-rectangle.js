#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print (row, col) {
    for (let x = 0, y; x < row; x++) {
      y = ' ';
      for (let g = 0; g < col; g++) {
        y += 'X';
      }
      console.log(y);
    }
  }
}
module.exports = Rectangle;
