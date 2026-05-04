'''Problem Description

A father wants to leave several sheep and chickens as an inheritance for his son. The son wants more sheep than chickens and asks how many of each there are. The father only tells him the total number of legs (N).

Your task is to determine the number of sheep and chickens based on the total number of legs, keeping in mind that the son wants to maximize the number of sheep.

Sheep have 4 legs.

Chickens have 2 legs.

Input

A single integer N (N≤10 
6
 ), representing the total number of legs.

Output

Two integers: the number of sheep and the number of chickens.'''
n=int(input())
koy=0
tauk=0
while n>=4:
    koy+=1
    n=n-4
while n>=2:
    tauk+=1
    n=n-2
print(koy,tauk)
    
