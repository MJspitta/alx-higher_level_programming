#!/usr/bin/node
const list = require('./100-data').list;
const listNew = list.map((i, idx) => i * idx);
console.log(list);
console.log(listNew);
