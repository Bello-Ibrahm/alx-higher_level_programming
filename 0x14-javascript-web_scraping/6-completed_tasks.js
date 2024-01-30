#!/usr/bin/node
const req = require('request');
const url = process.argv[2];

req.get(url, (err, res, content) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(content);
    const completedTaskObj = {};

    tasks.forEach((item) => {
      if (item.completed) {
        if (!completedTaskObj[item.userId]) {
          completedTaskObj[item.userId] = 1;
        } else {
          completedTaskObj[item.userId] += 1;
        }
      }
    });
    console.log(completedTaskObj);
  }
});
