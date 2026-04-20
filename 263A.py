for i in range(5):
    rows=list(map(int,input().split()))
    for j in range(5):
        if rows[j]==1:
            moves=abs(i-2)+abs(j-2)
            print(moves)
            break
