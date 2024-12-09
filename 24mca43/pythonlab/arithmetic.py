
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
sum=n1+n2
difference=n1-n2
product=n1*n2
division=0
modulus=0
if(n2!=0):
	division=n1/n2
	modulus=n1%n2
	print(f"Division:{n1}/{n2}={division}") 
	print(f"Modulus:{n1}%{n2}={modulus}")

else:
	print("Division and modulus Not possible")

exponent=n1**n2
print(f"Sum:{n1}+{n2}={sum}")
print(f"Difference:{n1}-{n2}={difference}")
print(f"Product:{n1}*{n2}={product}")
print(f"Exponent:{n1}**{n2}={exponent}")
