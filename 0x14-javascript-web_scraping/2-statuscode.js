#!/usr/bin/node
const req = require('request');
const url = process.argv[2];

req.get(url, 'utf-8', (err, content) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${content.statusCode}`);
  }
});
