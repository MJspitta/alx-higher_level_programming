#!/usr/bin/node

const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/';

request.get(url + process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
