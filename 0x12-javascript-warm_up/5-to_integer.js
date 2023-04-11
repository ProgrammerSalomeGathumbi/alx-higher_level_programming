#!/usr/bin/node
const i = parseInt(process.argv[2]);
if (i) {
  console.log('My Number: ' + i);
} else {
  console.log('Not a number');
}
