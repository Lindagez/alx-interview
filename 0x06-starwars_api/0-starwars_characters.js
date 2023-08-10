#!/usr/bin/node

const request = require('request');

const getCharacters = (movieId) => {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Failed to get characters: ${response.statusCode}`);
      return;
    }

    const data = JSON.parse(body);
    const characters = data.characters;
    for (const character of characters) {
      console.log(character.name);
    }
  });
};

if (process.argv.length !== 2) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  return;
}

const movieId = process.argv[2];
getCharacters(movieId);

