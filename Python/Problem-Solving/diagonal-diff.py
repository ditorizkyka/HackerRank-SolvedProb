
import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    # Write your code here
    toRight = 0
    for i in range(len(arr)):
        toRight = arr[i][i] + toRight
    
    toLeft = 0
    size = len(arr) - 1
    for i in range(len(arr)):
        toLeft = arr[size-i][i] + toLeft

    return abs(toRight-toLeft)

if __name__ == '__main__':


    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
