q,s=map(int,input().split())
y=list(map(int,input().split()))
for j in range (0,s):
    y=[y[-1]]+y[:-1]
print(*y,end='')
