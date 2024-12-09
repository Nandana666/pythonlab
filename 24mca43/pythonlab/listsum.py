nlist=[]
n=int(input("Enter no.of element:"))
for i in range (n):
	num=int(input("Enter the numbers:"))
	nlist.append(num)
sum=0
for i in nlist:
	sum+=i
print("Sum of all items in the list:",sum)
