#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const complete = {};

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const text = JSON.parse(body);
  text.forEach(task => {
    if (task.completed) {
      const user = task.userId;
      if (user in complete) {
        complete[user]++;
      } else {
        complete[user] = 1;
      }
    }
  });
  console.log(complete);
});
