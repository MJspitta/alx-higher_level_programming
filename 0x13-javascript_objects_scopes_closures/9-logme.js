#!/usr/bin/node
let counter = -1;
exports.logMe = function (item) {
  counter += 1;
  console.log(counter + ': ' + item);
};
