n=int(input("Enter the limit:"))
for i in range(1,n):
	temp=i
	sum=0
	r=0
	while temp>0:
		print(num)
		r=num%10
		num=num//10
		sum=sum+r
flag=0
if sum<=1:
	continue
for j in range(2,sum):
	if sum%j==0:
		flag=1
if flag==0:
	print("Sum of ",i,"=",sum)
