#!/usr/bin/node

const args = process.argv.slice(2);
const firstArgument = parseInt(args[0]);

if (isNaN(firstArgument)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${firstArgument}`);
}
