#!/usr/bin/node

const SquareS = require('./5-square.js');

class Square extends SquareS {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0, a; i < this.height; i++) {
      a = '';
      for (let x = 0; x < this.width; x++) {
        a += c;
      }
      console.log(a);
    }
  }
}
module.exports = Square;
