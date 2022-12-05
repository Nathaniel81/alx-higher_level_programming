#!/usr/bin/node

const argv = process.argv;

if (isNaN(argv[2]) || !argv[2]) {
	console.log('Not a number');
} else {
	console.log('My Number: ' + argv[2]);
}
