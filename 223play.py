    
deepa1=int(input())
Sum=0
dig=0
while(deepa1>0):
	dig=deepa1%10
	Sum+=dig*dig
	deepa1=deepa1//10
print(Sum)	
