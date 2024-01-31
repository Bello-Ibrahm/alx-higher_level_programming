#!/usr/bin/node
const req = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

req.get(url, (err, res, content) => {
  if (!err) {
    const data = JSON.parse(content);
    const characters = data.characters;
    // console.log(characters);
    printCharacters(characters, 0);
  }
});

const printCharacters = (characters, idx) => {
  req.get(characters[idx], (err, res, content) => {
    if (!err) {
      console.log(JSON.parse(content).name);
      if (idx + 1 < characters.length) {
        printCharacters(characters, idx + 1);
      }
    }
  });
};
