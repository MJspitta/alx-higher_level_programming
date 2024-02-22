#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async function (err, resp, body) {
  const arr = [];

  if (err) {
    console.log(err);
  } else {
    const film = JSON.parse(body);
    for (let i = 0; i < film.characters.length; i++) {
      arr.push(myCharac(film.characters[i]));
    }
  }

  let actors = await Promise.all(arr);

  actors = actors.map((actor) => JSON.parse(actor).name);
  actors.forEach((actor) => console.log(actor));
});

function myCharac (charac) {
  return new Promise((resolve, reject) => {
    request(charac, function (err, resp, body) {
      if (err) {
        reject(err);
      }
      resolve(body);
    });
  });
}
