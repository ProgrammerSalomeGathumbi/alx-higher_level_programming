#!/usr/bin/node
const i = parseInt(process.argv[2]);
const n = 'X';
let y;
let z;
if (i) {
  for (y = 0; y < i; y++) {
    for (z = 0; z < i; z++) {
      process.stdout.write(n);
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
