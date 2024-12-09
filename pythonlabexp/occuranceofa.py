n=int(input("Enter no. of names:"))
name=[]
count=0
for i in range(n):
	f=input("Enter names:")
	name.append(f)
for i in name:
	for j in i:
		if j=='a' or j=='A':
			count=count+1
print("Total count:",count)
