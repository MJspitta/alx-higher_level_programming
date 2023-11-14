#!/usr/bin/node
const num = parseInt(process.argv[2], 10);
function facto (n) {
  if (isNaN(n) || n === 0) {
    return (1);
  }
  return (n * facto(n - 1));
}
console.log(facto(num));
