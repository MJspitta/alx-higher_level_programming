#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  let begin = 0;
  const end = list.length - 1;
  for (begin = 0; begin < list.length; begin++) {
    revList.push(list[end - begin]);
  }
  return revList;
};
