a,b=map(int,input().split())
num=list(map(int,input().split()))
count=0
for i in range(a):
    th = num[b-1]
    if num[i]>=th and num[i]>0:
        count+=1
print(count)
