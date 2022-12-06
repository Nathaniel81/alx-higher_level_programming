#!/usr/bin/node

const args = process.argv;
let fstbig = parseInt(args[2]);
let idx = 2;

if (args.length < 4) {
	console.log(0);
} else {
	for (let i = 3; i < args.length; i++) {
		if (fstbig < args[i]){
			fstbig = args[i];
			idx = i;
		}
	}
	args.splice(idx, 1);
	let scndbig = parseInt(args[2]);

	for (let i = 3; i < args.length; i++) {
		if (scndbig < args[i]){
			scndbig = args[i];
		}
	}
	console.log(scndbig);
	}
