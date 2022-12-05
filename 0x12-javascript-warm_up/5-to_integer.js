#!/usr/bin/node

const av = parseInt(process.argv[2]);
if (process.argv[2] === undefined || isNaN(av)) {
	console.log('Not a number');
} else {
	console.log('My Number: ' + av);
}
