n=int(input("Enter a number:"))
print("Factors of ",n)
i=1
while(i<=n):
	if n%i==0:
		print(i,end=" ")
	i+=1

