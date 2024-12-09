n=int(input("Enter a number:"))
num1=n
num2=0
r=0
while (n!=0):
	r=n%10
	num2=(num2*10)+r
	n=n//10
print(num2)
if num1==num2:
	print(num1,"is a palindrome number")
else:
	print(num1,"is not a palindrome number")
