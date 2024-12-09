import math
n=int(input("Enter a number:"))
if n<0:
	print("Negative number does not have factorial")
else:
	f=math.factorial(n)
	print("Factorial of ",n,"is",f)
