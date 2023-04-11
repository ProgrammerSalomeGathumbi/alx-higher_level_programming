#!/usr/bin/node
const i = process.argv;
const y = i.length;
if (y <= 3) {
  console.log(0);
} else {
  const x = i.map(Number).sort(function(a, b) {return b - a});
  const y = x.slice(3);
  console.log(y[0]);
}
