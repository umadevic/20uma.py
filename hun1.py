y1=int(input())
t1=0
lst=input().split()
lst=list(map(int,lst))
new=[]
for i in range(0,n1):
    if((lst.count(lst[i]))>=2):
      if lst[i] not in new:
        new.append(lst[i])
        t1=1
if(t1==0):
  print("unique")
else:
  for i in range(0,y1):
    print(min(new),end=" ")
    new.remove(min(new))
