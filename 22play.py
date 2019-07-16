u,m=map(int,input().split())
a=list(map(int,input().split()))
for m in range (0,j):
    a=[a[-1]]+a[:-1]
print(*a,end='')
