integerlist=[]
n=int(input("Enter no.of elements:"))
for i in range(n):
	integer=int(input("Enter the number:"))
	integerlist.append(integer)
result=[]
for num in integerlist:
	if num>100:
		result.append("over")
	else:
		result.append(num)
print("Result:",result)
