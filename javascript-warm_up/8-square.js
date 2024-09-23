#!/usr/bin/node

const args = process.argv;
const size = parseInt(args[2], 10);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
