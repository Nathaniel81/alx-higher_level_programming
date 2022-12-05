#!/usr/bin/node

const Argv = process.Argv;
if (Argv[2]) {
  console.log(Argv[2]);
} else {
  console.log('No argument');
}
