n=int(input())
for i in range(1,n+1):
    x=input()
    if len(x)>10:
        print(f"{x[0]}{(len(x)-2)}{x[-1]}")
    else:
        print(x)
