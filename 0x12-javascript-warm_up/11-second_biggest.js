#!/usr/bin/node
const len = process.argv.length;
function comp (x, y) {
  return (y - x);
}
if (len <= 3) {
  console.log(0);
} else {
  console.log(process.argv.slice(2).sort(comp)[1]);
}
