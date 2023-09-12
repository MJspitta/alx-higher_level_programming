#!/usr/bin/node
let i;
const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
