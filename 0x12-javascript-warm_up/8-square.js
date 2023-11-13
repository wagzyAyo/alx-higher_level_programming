#!/usr/bin/node

if (!isNaN(parseInt(process.argv[2]))) {
  for (let row = 0; row < process.argv[2]; row++) {
    let a = '';
    for (let col = 0; col < process.argv[2]; col++) {
      a += 'X';
    }
    console.log(a);
  }
} else {
  console.log('Missing size');
}
