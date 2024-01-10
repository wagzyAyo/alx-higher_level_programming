#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const tasks = {};
    const response = JSON.parse(body);
    for (let i = 0; i < response.length; i++) {
      if (response[i].completed === true) {
        if (tasks[response[i].userId] === undefined) {
          tasks[response[i].userId] = 0;
        }
        tasks[response[i].userId]++;
      }
    }
    console.log(tasks);
  }
});
