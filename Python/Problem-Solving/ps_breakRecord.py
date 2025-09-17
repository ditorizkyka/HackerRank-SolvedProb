import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
   
    for i in range(len(scores)):
        print(i, scores[i])
        if i == 0:
            min_score = scores[i]
            max_score = scores[i]
            min_count = 0
            max_count = 0
        elif scores[i] < min_score:
            min_score = scores[i]
            min_count += 1
        elif scores[i] > max_score:
            max_score = scores[i]
            max_count += 1
    return [max_count, min_count]
    # Write your code here

if __name__ == '__main__':
    

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
