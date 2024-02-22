#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else if (resp.statusCode === 200) {
    const film = JSON.parse(body).results;
    let num = 0;
    for (const i in film) {
      const charac = film[i].characters;
      for (const c in charac) {
        if (charac[c].includes('18')) {
          num++;
        }
      }
    }
    console.log(num);
  } else {
    console.log('Error Code:' + resp.statusCode);
  }
});
