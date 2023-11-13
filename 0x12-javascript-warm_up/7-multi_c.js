#!/usr/bin/node

const myVar = 'C is fun';
if (!isNaN(parseInt(process.argv[2]))) {
  for (let x = 0; x < process.argv[2]; x++) {
    console.log(myVar);
  }
} else {
  console.log('Missing number of occurrences');
}
