'''
You are given two integers a and b.

Consider all integers from a to b (inclusive) in increasing order.

For each integer i, output:

"Woosong!" if i is divisible by 3
"University!" if i is divisible by 5
"Kazakhstan!" if i is divisible by 7
if divisible by 3 and 5 → "Woosong University!!"
if divisible by 3 and 7 → "Woosong Kazakhstan!!"
if divisible by 5 and 7 → "University Kazakhstan!!"
if divisible by 3, 5, and 7 → "Woosong University Kazakhstan!!!"
if i is not divisible by 3, 5, or 7, output the number followed by a dot "."
Input
Two integers a and b, each on a separate line (1≤𝑎,𝑏≤105).

Output
Each result must be printed on a separate line.

Examples
inputCopy
1
35
outputCopy
1.
2.
Woosong!
4.
University!
Woosong!
Kazakhstan!
8.
Woosong!
University!
11.
Woosong!
13.
Kazakhstan!
Woosong University!!
16.
17.
Woosong!
19.
University!
Woosong Kazakhstan!!
22.
23.
Woosong!
University!
26.
Woosong!
Kazakhstan!
29.
Woosong University!!
31.
32.
Woosong!
34.
University Kazakhstan!!
inputCopy
111
99
outputCopy
Woosong!
University!
101.
Woosong!
103.
104.
Woosong University Kazakhstan!!!
106.
107.
Woosong!
109.
University!
Woosong!'''
a=int(input())
b=int(input())
start=min(a,b)
end=max(a,b)
for i in range(start,end+1):
    if i%3==0 and i%5==0 and i%7==0:
        print("Woosong University Kazakhstan!!!")
    elif i%5==0 and i%7==0:
        print("University Kazakhstan!!")
    elif i%3==0 and i%7==0:
        print("Woosong Kazakhstan!!")
    elif i%3==0 and i%5==0:
        print("Woosong University!!")
    elif i%3==0:
        print("Woosong!")
    elif i%5==0:
        print("University!")
    elif i%7==0:
        print("Kazakhstan!")
    else:
        print(f"{i}.")
