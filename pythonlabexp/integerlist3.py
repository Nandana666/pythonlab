n1=int(input("Enter no. of inetgers in list1:"))
n2=int(input("Enter no.of integers in list2:"))
list1=[]
list2=[]
print("List1")
for i in range(n1):
	integer=int(input("Enter value:"))
	list1.append(integer)
print("List2")
for i in range(n2):
        integer=int(input("Enter value:"))
        list2.append(integer)
if len(list1)==len(list2):
	print("Lists are of the same length")
else:
	print("Lists are not in same length")
if sum(list1)==sum(list2):
	print("Lists have same sum value")
else:
	print("Lists sums are not same")
f=0
for i in list1:
	if integer in list2:
		f=1
if f!=1:
	print("There is no common value")
else:
	print("There is common value")
