#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const path = process.argv[3];

request(URL, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(path, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
