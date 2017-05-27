# an array is said to be a balanced array if the sum of al elements in the left half of the array is equal to the sum of all elements in the right half. 

# We need to find the minimum value to be added to any one of the array elements to make the array balanced

# input format:

# first line contains an even integer n
# second line contains n space separated integers

#!/bin/python3

import sys

def solve(a):
    l=len(a)
    half=int(l/2)
    leftSum=0
    rightSum=0

    print(half)
    print(l)

    for i in range(half):
        leftSum+=int(a[i])
    for i in range(half,l):
        rightSum+=int(a[i])
    return abs(rightSum-leftSum)


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = solve(a)
print(result)
