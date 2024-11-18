'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on('end', function () {
  inputString = inputString.split('\n');

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function plusMinus(arr) {
  let positive = 0;
  let minus = 0;
  let zero = 0;
  for (let index = 0; index < arr.length; index++) {
    const element = arr[index];
    if (element > 0) {
      positive++;
    } else if (element < 0) {
      minus++;
    } else {
      zero++;
    }
  }
  console.log(positive / arr.length)
  console.log(minus / arr.length)
  console.log(zero / arr.length)

}

function main() {
  const n = parseInt(readLine().trim(), 10);

  const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

  plusMinus(arr);
}
