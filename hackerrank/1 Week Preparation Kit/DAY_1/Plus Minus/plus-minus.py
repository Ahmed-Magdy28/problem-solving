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
    postive = 0
    negtive = 0
    zero = 0
    for num in arr:
        if (num > 0):
            postive += 1
        elif (num < 0):
            negtive += 1
        else:
            zero += 1

    print(f"{(postive / length):.6f}\n{(negtive / length):.6f}\n{(zero / length):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
