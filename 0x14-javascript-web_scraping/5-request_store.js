#!/usr/bin/node
const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];

req.get(url, (err, res, content) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filepath, content, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
