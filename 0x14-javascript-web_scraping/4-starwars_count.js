#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
const charId = '18';
let count = 0;

req.get(url, (err, res, content) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(content);
    data.results.forEach(item => {
      item.characters.forEach(character => {
        if (character.includes(charId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
