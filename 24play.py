    
#v
i=input()
b=str(input())
p=('a','e','i','o','u')
for i in b:
    if i in p:
        b=b.replace(i,"")
print(b[::-1])
