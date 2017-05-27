#!/bin/python3

import sys
import math

"""
This is an interesting problem. Get a string of numbers in the first line of input. In the second line are 3 values k, b and m, k is the length of substrings we need to get of s, we need to find all substrings of s from the starting point( in order of the sequence of numbers in the string: 122231-> for k = 4, it is: 1222, 2223, 2231), b is a base in which the substrings are supposed to be in, they need to be changed from that base to base 10, then m is the modulo value for base 10 numbers obtained the final magic number is the sum of all such numbers obtained.
"""

# class Node:
#     def __init__(self, val):
#         self.val=val
#         next=None

#     def getNext(self):
#         return self.next

#     def getVal(self):
#         return self.val

#     def setNext(self, next):
#         self.next=next

#     def setVal(self, val):
#         self.val=val

def getBase10Num(num, base):
    # here num is a string
    n=[]
    place=0
    for i in range(len(num)-1,-1,-1):
        val=int(num[i])
        try:
            n.append(int(val * math.pow(base, place)))
        except Exception:
            print('oops')
        place+=1 

    return n

def getMagicNumber(s, k, b, m):
    substrings=[]
    i=0
    while (i+k)<=len(s):
        substrings.append(s[i:i+k])
        i+=1
    # print(substrings)
    base10Num=[]
    for i in substrings:
        base10Num.append(getBase10Num(i,b))
    # print(base10Num)
    moduloNum=[]
    addition=0
    for i in base10Num:
        addition=0
        # print('i now:'+str(i))
        try:
            for j in i:
                addition+=(j%m)
            moduloNum.append(addition%m)
        except Exception:
            print('oops')
        
    # print(moduloNum)
    s=0
    for i in moduloNum:
        s+=i

    return s 

s = input().strip()
k, b, m = input().strip().split(' ')
k, b, m = [int(k), int(b), int(m)]
result = getMagicNumber(s, k, b, m)
print(result)