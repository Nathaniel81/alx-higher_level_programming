#!/usr/bin/node

const argv = parseInt(process.argv[2]);

if (isNaN(argv) || process.argv[2] === undefined) {
	console.log('Not a number');
} else {
	console.log('My Number: ' + argv);
}
