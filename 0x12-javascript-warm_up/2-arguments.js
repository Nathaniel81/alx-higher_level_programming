#!/usr/bin/node

if (process.argv.length === 3){
	console.log('Argument passed');
} else if (process.argv.length === 2){
	console.log('No arguments');
} else {
	console.log('Arguments found');
}
