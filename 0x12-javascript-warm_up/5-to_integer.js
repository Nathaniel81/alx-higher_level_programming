#!/usr/bin/node

const argv = process.argv;

if (parseInt(argv[2]) === NaN || !argv[2]) {
	console.log('Not a number');
} else {
	console.log('My Number: ' + parseInt(argv[2]));
}
