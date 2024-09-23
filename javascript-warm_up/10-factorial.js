#!/usr/bin/node

const args = process.argv;
const n = parseInt(args[2], 10);

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(n));
