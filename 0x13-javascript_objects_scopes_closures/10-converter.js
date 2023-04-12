#!/usr/bin/node
exports.converter = function (base) {
  function numberArg (i) {
    return (i.toString(base));
  }
  return (numberArg);
};
