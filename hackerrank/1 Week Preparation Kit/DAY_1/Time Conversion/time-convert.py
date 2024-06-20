#!/usr/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = int(f"{s[0]}{s[1]}")
    min = int(f"{s[3]}{s[4]}")
    sec = int(f"{s[6]}{s[7]}")
    time = f"{s[8]}{s[9]}"
    if time == "AM" and hour == 12:
        hour = "00"
        if min < 10:
            min = f"0{min}"
        if sec < 10:
            sec = f"0{sec}"
    elif time == "PM":
        if hour != 12:
            hour += 12
        if min < 10:
            min = f"0{min}"
        if sec < 10:
            sec = f"0{sec}"
    else:
        if hour < 10:
            hour = f"0{hour}"
        if min < 10:
            min = f"0{min}"
        if sec < 10:
            sec = f"0{sec}"
    new_time = f"{hour}:{min}:{sec}"
    return new_time
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()