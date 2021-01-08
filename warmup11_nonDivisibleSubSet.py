
"""Given a set of distinct integers, print the size of a maximal subset of S where the sum of 2 any numbers in S1 is not evenly divisible by K.

For example, the array S = [19, 10, 12, 10, 24, 25, 22] and k = 4. One of the arrays that can be created is S1[0] = [10, 12, 25]. Another is S1[1] = [19,22,24]. After testing all permutations, the maximum length solution array has 3 elements.

Function Description
Complete the nonDivisibleSubset function in the editor below. It should return an integer representing the length of the longest subset of S meeting the criteria.

nonDivisibleSubset has the following parameter(s):
- S: an array of integers
- k: an integer

Input Format
The first line contains 2 space-separated integers, n and k, the number of values in S and the non factor.
The second line contains n space-separated integers describing S[i], the unique values of the set.

Constraints
- 1 <= n <= 100 a la 5ta
- 1 <= k <= 100
- 1 <= S[i] <= 10 a la novena
- All of the given numbers are distinct.

Output Format
Print the size of the largest possible subset (S1).

Sample Input
4 3
1 7 2 4

Sample Output
3

Explanation
The sums of all permutations of two elements from S = {1,7,2,4} are:
1 + 7 = 8
1 + 2 = 3
1 + 4 = 5
7 + 2 = 9
7 + 4 = 11
2 + 4 = 6

We see that only S1 = {1,7,4} will not ever sum to a multiple of k = 3.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()