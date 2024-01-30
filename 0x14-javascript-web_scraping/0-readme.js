#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];

fs.readFile(filepath, 'utf-8', (err, content) => {
  if (err) {
	  console.log(err);
  }else {
	  console.log(content.toString());
  }
});
