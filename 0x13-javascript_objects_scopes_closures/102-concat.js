#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');
const text1 = fs.readFileSync(fileA, 'utf8');
const text2 = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, text1 + text2);
