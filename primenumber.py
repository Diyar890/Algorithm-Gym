'''W.4.4. Prime number
time limit per test0.25 seconds
memory limit per test4 megabytes
You are given a single integer 𝑛.

Your task is to determine whether n is a prime number.

A number is prime if it is greater than 1 and divisible only by 1 and itself.

Input
A single integer 𝑛 (0≤𝑛≤109).

Output
Print YES if n is a prime number. Otherwise, print NO.

Examples
inputCopy
7
outputCopy
YES
inputCopy
8
outputCopy
NO'''
import math
n=int(input())
div=-1
for i in range(2,int(math.sqrt(n)+1)):
    if n%i==0:
        div=i
if div==-1:
    print("YES")
else:
    print("NO")
