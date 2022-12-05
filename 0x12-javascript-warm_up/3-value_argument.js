#!/usr/bin/node

const Args = process.argv;

if (Args[2] === undefined) {
	console.log('No argument');
} else {
	console.log(process.argv[2]);
}
