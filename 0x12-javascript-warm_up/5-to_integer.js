#!/usr/bin/node
const i = parseInt(process.argv[2]);
if (!i) {
  console.log('Not a number');
} else {
  console.log('My Number: ' + i);
}
