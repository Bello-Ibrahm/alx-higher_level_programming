#!/usr/bin/node
// To use axios =>  npm install axios

const req = require('axios');
const url = process.argv[2];

req.get(url)
  .then(res => {
    console.log(`Code: ${res.status}`);
    // Print the response data if needed
    // console.log(res.data);
  })
  .catch(err => {
    console.log(err);
  });
