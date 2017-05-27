#!/bin/python3

import sys

"""
This is an interesting problem. Get a string of numbers in the first line of input. In the second line are 3 values k, b and m, k is the length of substrings we need to get of s, we need to find all substrings of s from the starting point( in order of the sequence of numbers in the string: 122231-> for k = 4, it is: 1222, 2223, 2231), b is a base in which the substrings are supposed to be in, they need to be changed from that base to base 10, then m is the modulo value for base 10 numbers obtained the final magic number is the sum of all such numbers obtained.
"""

def getMagicNumber(s, k, b, m):
            

s = input().strip()
k, b, m = input().strip().split(' ')
k, b, m = [int(k), int(b), int(m)]
result = getMagicNumber(s, k, b, m)
print(result)