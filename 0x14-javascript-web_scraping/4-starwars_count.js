#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

request(URL, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let i = 0;
    for (const movie of JSON.parse(body).results) {
      for (const wedgeMovies of movie.characters) {
        if (wedgeMovies.split('18').length === 2) {
          i++;
        }
      }
    }
    console.log(i);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
