#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = '/18/';

request(apiUrl, function (error, response, body) {
  if (error) console.error(error);
  let count = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      count += (character.includes(characterId) ? 1 : 0);
    }
  }
  console.log(count);
});
