#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const URL = 'https://swapi-api.alx-tools.com/api/films/';

request(URL + movieId, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
