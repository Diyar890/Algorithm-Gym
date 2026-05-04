'''Problem Description
Eregali aga doesn't like walking. To get to his destination by bus, he comes from his house to a bus stop. Bus stops are located at equal distances of K meters from each other (i.e., at positions 0,K,2K,3K,…).
Eregali aga's house is located at the N-meter mark along that bus route. You need to find the minimum distance he needs to walk to reach the nearest bus stop.
Input

You are given two values, K and N, on two separate lines:

1≤K≤2×10 
9
 

1≤N≤2×10 
9
Output
Print a single integer: the distance to the nearest bus stop.
Example
Input:

Plaintext
1000
4300
Output:

Plaintext
300
Note (Explanation)

In the first example, bus stops are located at 0,1000,2000,3000,4000,5000,… meters. Eregali aga's house is at 4300 meters.

The previous stop is at 4000 m (distance = 300 m).

The next stop is at 5000 m (distance = 700 m).
The nearest one is 4000 m, so he needs to walk 300 meters back.'''
k=int(input())
n=int(input())
tt=n%k
s=k-tt
print(min(s,tt))
