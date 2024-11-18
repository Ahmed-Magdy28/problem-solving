"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString: string = "";
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on("data", function (inputStdin: string): void {
  inputString += inputStdin;
});

process.stdin.on("end", function (): void {
  inputLines = inputString.split("\n");
  inputString = "";

  main();
});

function readLine(): string {
  return inputLines[currentLine++];
}

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function plusMinus(arr: number[]): void {
  let positive = 0;
  let minus = 0;
  let zero = 0;
  for (let index = 0; index < arr.length; index++) {
    const element = arr[index];
    if (element > 0) {
      positive = positive + 1;
    } else if (element < 0) {
      minus = minus + 1;
    } else {
      zero++;
    }
  }
  console.log(positive / arr.length);
  console.log(minus / arr.length);
  console.log(zero / arr.length);
}

function main() {
  const n: number = parseInt(readLine().trim(), 10);

  const arr: number[] = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((arrTemp) => parseInt(arrTemp, 10));

  plusMinus(arr);
}
