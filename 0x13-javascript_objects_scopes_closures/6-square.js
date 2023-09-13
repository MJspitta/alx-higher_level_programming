#!/usr/bin/node
const BaseSquare = require('./5-square');
module.exports = class Square extends BaseSquare {
  charPrint (c) {
    if (c) {
      let i;
      for (i = 0; i < this.width; i++) {
        console.log('C'.repeat(this.height));
      }
    } else {
      super.print();
    }
  }
};
