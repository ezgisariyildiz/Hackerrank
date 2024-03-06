#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    lis=list(s.split())
    for i in range(len(lis)):
        s=s.replace(lis[i],lis[i].capitalize())

    # lis[i].capitalize()
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()