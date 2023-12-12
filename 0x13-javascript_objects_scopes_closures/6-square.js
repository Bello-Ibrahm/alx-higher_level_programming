#!/usr/bin/node

/**
 * Square class that inherits from previous square class
 */
const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
