#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

const characterUrl = `${apiUrl}people/${characterId}`;

request.get(characterUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const character = JSON.parse(body);
      const movieCount = character.films.length;
      console.log(movieCount);
    } else {
      console.error(response.statusCode);
    }
  }
});
