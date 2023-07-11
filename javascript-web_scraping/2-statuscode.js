#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error('code: %s', error);
  } else {
    console.log('code: %s', response.statusCode);
  }
});
