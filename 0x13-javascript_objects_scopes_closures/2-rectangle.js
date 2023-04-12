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
};
