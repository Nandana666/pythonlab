n=int(input("Enter the upperlimit:"))
sum=0
for i in range(1,n):
	if i%6==0 and i%4!=0:
		sum+=i
print("Sum=",sum)
