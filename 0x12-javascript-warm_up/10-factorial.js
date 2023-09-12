#!/usr/bin/node
const x = parseInt(process.argv[2]);
function factorial (x) {
  if (isNaN(x) || x === 0) {
    return (1);
  } else {
    x *= factorial(x - 1);
    return (x);
  }
}
console.log(factorial(x));
