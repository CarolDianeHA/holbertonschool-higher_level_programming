#!/usr/bin/node

const args = process.argv.slice(2);
const numArguments = args.length;

if (numArguments === 0 || numArguments === 1) {
  console.log(0);
} else {
  const numbers = args.map(Number).sort((a, b) => b - a);
  const secondBiggest = numbers[1];
  console.log(secondBiggest);
}
