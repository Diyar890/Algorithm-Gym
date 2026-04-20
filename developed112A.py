import sys
data=sys.stdin.read().split()
if len(data)>=2:
    s1=data[0].lower()
    s2=data[1].lower()
    if s1<s2:
        print("-1")
    elif s1>s2:
        print("1")
    elif s1==s2:
        print("0")
        
