#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (err, text) {
  if (text === undefined) {
    console.log(err);
  } else {
    console.log(text);
  }
});
