integerlist=[]
n=int(input("Enter no.of elements:"))
for i in range(n):
        integer=int(input("Enter the number:"))
        integerlist.append(integer)
newlist=[]
for num in integerlist:
	if num%2!=0 :
		newlist.append(num)
print("Result:",newlist)
