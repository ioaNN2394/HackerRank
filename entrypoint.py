#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'performOperations' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER_ARRAY op
#

def performOperations(N, op):
    # Initialize the array as an identity permutation
    array = list(range(1, N + 1))
    result = []
    
    for operation in op:
        if operation in array:
            # Swap the first and last elements
            array[0], array[-1] = array[-1], array[0]
        else:
            # Remove the last element and push operation to the end
            array = array[:-1] + [operation]
        
        # Add the sum of the elements of the array to the result
        result.append(sum(array))
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    N = int(first_multiple_input[0])

    M = int(first_multiple_input[1])

    op = []

    for _ in range(M):
        op_item = int(input().strip())
        op.append(op_item)

    result = performOperations(N, op)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()