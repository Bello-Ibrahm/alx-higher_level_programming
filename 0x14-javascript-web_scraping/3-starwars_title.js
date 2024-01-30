#!/usr/bin/node
const req = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

req.get(url, 'utf-8', (err, res, content) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(content).title);
  }
});
