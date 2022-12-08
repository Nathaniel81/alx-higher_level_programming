#!/usr/bin/node
const theList = require('./100-data').list;

const newList = theList.map(lst => lst * (theList.indexOf(lst)));
console.log(theList);
console.log(newList);
