n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))
if n1>n2 and n1>n3:
	print(f"{n1} is greatest")
elif n2>n3 and n2>n1:
	print(f"{n2} is greatest")
else:
	print(f"{n3} is greatest")
