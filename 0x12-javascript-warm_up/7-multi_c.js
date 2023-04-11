#!/usr/bin/node
const i = parseInt(process.argv[2]);
const x = 'C is fun';
let y = 0;
if (i) {
  while (y < i) {
    console.log(x);
    y++;
  }
} else {
  console.log('Missing number of occurrences');
}
