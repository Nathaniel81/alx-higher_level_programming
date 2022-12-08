#!/usr/bin/node
exports.esrever = function (list) {
  let myList = [], j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    myList[j] = list[i];
      j++;
  }
  return myList;
};
