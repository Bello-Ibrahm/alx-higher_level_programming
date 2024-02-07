#!/usr/bin/node
const req = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

req.get(url, (err, res, content) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(content);
    const characters = data.characters;
    characters.forEach((character) => {
      // console.log(character);
      req.get(character, (err, res, content) => {
        if (err) {
          console.log(err);
          return;
        }
        const characterData = JSON.parse(content);
        console.log(characterData.name);
      });
    });
  }
});
