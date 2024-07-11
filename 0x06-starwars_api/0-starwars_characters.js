#!/usr/bin/node

/**
 * This script fetches and prints the names of all characters
 * from a specified Star Wars film.
 *
 * Usage: ./0-starwars_characters.js <film_id>
 * Example: ./0-starwars_characters.js 3
 *
 * film_id: The ID of the Star Wars film to fetch characters from.
 *          Valid IDs range from 1 to 6 (corresponding to Episodes I to VI).
 */

const request = require('request');

// Wrap the request function in a Promise
const requestPromise = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, response, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

// Fetch the film data
request(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      console.error('Error fetching film:', err);
    } else {
      const chars = JSON.parse(body).characters; // Array of character URLs

      // Array of Promises
      const promises = chars.map((url) => requestPromise(url));

      // Wait for all Promises to resolve
      Promise.all(promises)
        .then((names) => {
          // Print all character names
          names.forEach((name) => console.log(name));
        })
        .catch((err) => {
          console.error('Error fetching character:', err);
        });
    }
  }
);
