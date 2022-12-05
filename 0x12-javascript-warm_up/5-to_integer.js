#!/usr/bin/node

const argv = process.argv;

if (isNaN(parseInt(argv[2])) || argv[2] === undefined) {
	console.log('Not a number');
} else {
	console.log('My Number: ' + argv[2]);
}
