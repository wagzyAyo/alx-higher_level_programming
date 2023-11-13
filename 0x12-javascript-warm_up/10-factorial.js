#!/usr/bin/node

function fact (x) {
  if (Number.isNaN(x) || x === 1) {
    return 1;
  } else {
    return fact(x - 1) * x;
  }
}
console.log(fact(parseInt(process.argv[2])));
