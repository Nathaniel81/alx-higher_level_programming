#!/usr/bin/node

const argv = process.argv;

if (parseInt(argv[2])) {
	console.log('My Number: ' + parseInt(argv[2]));
} else {
	console.log('Not a number');
}
