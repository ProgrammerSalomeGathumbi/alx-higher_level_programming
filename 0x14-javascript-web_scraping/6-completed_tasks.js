#!/usr/bin/node
const request = require('request');

const URL = process.argv[2];

request(URL, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
  } else {
    const todos = JSON.parse(body);
    const doneTasks = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (doneTasks[todo.userId]) {
          doneTasks[todo.userId]++;
        } else {
          doneTasks[todo.userId] = 1;
        }
      }
    });

    console.log(doneTasks);
  }
});
