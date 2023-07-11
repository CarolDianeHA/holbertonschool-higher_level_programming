#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = ('https://swapi-api.hbtn.io/api/films/' + movieId);

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      console.log(movie.title);
    }
  }
});
