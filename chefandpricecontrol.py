t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    x = sum(l)
    tot = 0
    for j in l:
        if j<=k:
            tot += j
        elif j>k:
            tot+=k
    res = x-tot
    print(res)      
