# ************ DAY5: MOCK TEST: PAIRS ************************


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    num_map = {}  # Numaraları ve hedef farklarını saklamak için bir hashmap
    pair_count = 0  # Çift sayısını saklamak için bir değişken

    # Her bir sayı için hashmap'e ekle
    for num in arr:
        num_map[num] = True

    # Her bir sayı için (sayı + hedef) değerini kontrol et
    for num in arr:
        target_plus = num + k
        # Eğer (sayı + hedef) değeri hashmap'te varsa, çifti say
        if target_plus in num_map:
            pair_count += 1

    return pair_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()