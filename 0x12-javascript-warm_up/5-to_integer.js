#!/usr/bin/node

const Argv = parseInt(process.argv[2]);

if (isNaN(Argv) || process.argv[2] === undefined) {
	console.log('Not a number');
} else {
	console.log('My Number: ' + Argv);
}
