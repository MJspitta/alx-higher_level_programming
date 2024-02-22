#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, resp, body) {
  if (!err) {
    const charac = JSON.parse(body).characters;
    charac.forEach((cha) => {
      request(cha, function (err, resp, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
