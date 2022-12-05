#!/usr/bin/node

if (process.argv.length >= 3){
	console.log('Argument passed');
} else if (process.argv.length < 3){
	console.log('No arguments');
}
