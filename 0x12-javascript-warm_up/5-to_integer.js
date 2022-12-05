#!/usr/bin/node

const Argv = parseInt(process.argv[2]);

if (process.argv[2] === undefined || isNaN(Argv)) {
	console.log('Not a number');
} else {
	console.log('My Number: ' + Argv);
}
