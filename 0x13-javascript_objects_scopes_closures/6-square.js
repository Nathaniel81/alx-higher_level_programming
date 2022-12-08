#!/usr/bin/node
const Squ = require('./5-square.js');

module.exports = class Square extends Squ {
  charPrint (c) {
    let chr;
    if (c === undefined) {
      chr = 'X';
    } else {
      chr = c;
    }
    for (let i = 0; i < this.width; i++) {
      console.log(chr.repeat(this.width));
    }
  }
};
