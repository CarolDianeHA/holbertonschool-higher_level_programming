#!/usr/bin/node
const argument = process.argv[2];
const number = parseInt(argument);

if (number) {
  for (let i = 0; i < number; i++) {
    let char = '';
    for (let j = 0; j < number; j++) {
      char += 'X';
    }
    console.log(char);
  }
} else {
  console.log('Missing size');
}
