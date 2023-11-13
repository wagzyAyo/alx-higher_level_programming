#!/usr/bin/node

const argc = process.argv

if (argc[2] === undefined) {
    console.log('No arguments')
} else {
    console.log(argc[2])
}
