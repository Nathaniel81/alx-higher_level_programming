#!/usr/bin/node

const Args = process.argv;

if (Args[2]) {
	console.log(Args[2]);
} else {
	console.log('No argument');
}
