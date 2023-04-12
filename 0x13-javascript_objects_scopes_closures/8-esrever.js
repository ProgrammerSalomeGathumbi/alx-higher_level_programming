#!/usr/bin/node
exports.esrever = function (list) {
  let x;
  const y = [];
  for (x = list.length - 1; x >= 0; x--) {
    y.push(list[x]);
  }
  return (y);
};
