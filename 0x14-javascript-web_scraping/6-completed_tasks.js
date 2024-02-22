#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else if (resp.statusCode === 200) {
    const dict = {};
    const tasks = JSON.parse(body);
    for (const t in tasks) {
      if (tasks[t].completed) {
        if (dict[tasks[t].userId] === undefined) {
          dict[tasks[t].userId] = 1;
        } else {
          dict[tasks[t].userId]++;
        }
      }
    }
    console.log(dict);
  } else {
    console.log('Error code: ' + resp.statusCode);
  }
});
