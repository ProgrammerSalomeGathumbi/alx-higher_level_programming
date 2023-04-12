#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let x;
      for (x = 0; x < this.height; x++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
