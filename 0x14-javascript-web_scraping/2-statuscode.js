#!/usr/bin/node
const req = require('request');
const url = process.argv[2];

req.get(url)
  .then(res => {
    console.log(`code: ${res.statusCode}`);
  })
  .catch(err => {
    console.log(err);
  });
