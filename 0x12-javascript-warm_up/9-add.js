#!/usr/bin/node
const num1 = parseInt(process.argv[2], 10);
const num2 = parseInt(process.argv[3], 10);

function add (x, y) {
  return (x + y);
}
console.log(add(num1, num2));
