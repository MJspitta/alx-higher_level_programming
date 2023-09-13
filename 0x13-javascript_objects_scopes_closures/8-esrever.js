#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  let first = 0;
  const last = list.length - 1;
  for (first; first < list.length; first++) {
    revList.push(list[last - first]);
  }
  return revList;
};
