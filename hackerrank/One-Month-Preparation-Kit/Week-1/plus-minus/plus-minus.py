#!/usr/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    length = len(arr)
    print(sum(1 for i in arr if i > 0) / length)
    print(sum(1 for i in arr if i < 0) / length)
    print(sum(1 for i in arr if i == 0) / length)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
