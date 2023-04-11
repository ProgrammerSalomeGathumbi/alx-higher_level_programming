#!/usr/bin/node
const i = process.argv;
const y = i.length;
if (y <= 3) {
  console.log(0);
} else {
  const x = i.slice(2).sort((a, b) => a - b);
  console.log(x[x.lenght - 2]);
}
