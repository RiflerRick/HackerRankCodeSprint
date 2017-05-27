#!/bin/python3

import sys

def getMagicNumber(s, k, b, m):
    # Complete this function
    

s = input().strip()
k, b, m = input().strip().split(' ')
k, b, m = [int(k), int(b), int(m)]
result = getMagicNumber(s, k, b, m)
print(result)
