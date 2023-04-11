#!/usr/bin/node
const i = parseInt(process.argv[2]);
function factorial (i) {
  if (i <= 1 || isNaN(i)) {
    return (1);
  } else {
    return (i * factorial(i - 1));
  }
}
console.log(factorial(i));
