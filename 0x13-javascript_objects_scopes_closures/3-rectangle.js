#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    const i = parseInt(w);
    const z = parseInt(h);
    if (i > 0 && z > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const a = 'X';
    let x;
    let y;
    for (x = 0; x < this.height; x++) {
      for (y = 0; y < this.width; y++) {
        process.stdout.write(a);
      }
      console.log('');
    }
  }
};
