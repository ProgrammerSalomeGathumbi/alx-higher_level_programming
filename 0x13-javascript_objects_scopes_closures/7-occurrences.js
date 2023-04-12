#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  let i;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      x++;
    }
  }
  return (x);
};
