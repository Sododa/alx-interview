#!/usr/bin/node

// Import the library
const request = require('request');

// Define URL of the Star Wars API
const API_URL = 'https://swapi-api.alx-tools.com/api';

// Check if the number of command line arguments is greater than 2
if (process.argv.length > 2) {
  // Make a resource for the specified film ID
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    // If the request, log the error
    if (err) {
      console.log(err);
    }
    // Get from the film's response body
    const charactersURL = JSON.parse(body).characters;

    // Create with the names of the characters
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        // Make character resource
        request(url, (promiseErr, __, charactersReqBody) => {
          // If an error reject the Promise with the error
          if (promiseErr) {
            reject(promiseErr);
          }
          // Resolve the character
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    // Wait for all separated by new lines
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
