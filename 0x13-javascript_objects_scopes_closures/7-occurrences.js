#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let number = 0;
  for (let x = 0; x < list.length; x++) {
    if (searchElement === list[x]) {
      number++;
    }
  }
  return number;
};
