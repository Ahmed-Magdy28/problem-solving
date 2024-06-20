#!/usr/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    big = arr[0]
    small = arr[0]
    all_sum = 0
    for num in arr:
        if (num > big):
            big = num
        if (num < small):
            small = num
        all_sum += num
    print(f"{all_sum - abs(big)} {all_sum - abs(small)}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
