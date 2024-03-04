import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Sort the array
    arr.sort()
    
    # Calculate the minimum sum
    min_sum = sum(arr[:4])
    
    # Calculate the maximum sum
    max_sum = sum(arr[1:])
    
    # Print the minimum and maximum sums
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)