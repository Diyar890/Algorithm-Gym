'''P.3.2B. Sum with Expression by Mod
time limit per test0.25 seconds
memory limit per test100 megabytes
You are given three integers a, b and c.

Consider all integers between a and b (inclusive) that are divisible by c.

If a<b, process these numbers in increasing order.
Otherwise, process them in decreasing order.
Your task is to print the full expression of their sum.

Input
A single line containing two integers (0≤𝑎,𝑏≤105,1≤𝑐≤105).

Output
Print the expression in the following format:

Numbers are joined by "+"
The last number is followed by "="
Then print the total sum
Finally, print "!"
Examples:
input:
1 15 2
output:
2+4+6+8+10+12+14=56!
input:
7 4 1
output:
7+6+5+4=22!'''
a,b,c=map(int,input().split())
san=[]
if a<=b:
    while a<=b and a%c!=0:
        a+=1
else:
    while a>=b and a%c!=0:
        a-=1
if a<b:
    for i in range(a,b+1,c):
        san.append(str(i))
else:
    for i in range(a,b-1,-c):
        san.append(str(i))
if san:
    tot=sum( int(x)  for x in san)
    s="+".join(san)
    print(f"{s}={tot}!")
