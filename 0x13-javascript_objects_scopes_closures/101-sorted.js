#!/usr/bin/node
const dict = require('./101-data.js').dict;
const dictNew = {};
for (const k in dict) {
  if (!dictNew[dict[k]]) {
    dictNew[dict[k]] = [k];
  } else {
    dictNew[dict[k]].push(k);
  }
}
console.log(dictNew);
