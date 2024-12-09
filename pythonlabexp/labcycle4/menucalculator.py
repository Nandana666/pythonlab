def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def mul(x,y):
	return x*y
def div(x,y):
	if y>0:
		return x/y
	else:
		print("Not posiible")
a=int(input("Enter first value:"))
b=int(input("Enter second value"))
while(1):
	print("MENU \n 1)Addition \n 2)Subtraction \n 3)Multiplication \n 4)Division")
	ch=int(input("Enter your choice:"))
	if ch==1:
		print("Sum=",add(a,b))
	elif ch==2:
		print("Difference=",sub(a,b))
	elif ch==3:
		print("Product=",mul(a,b))
	elif ch==4:
		print("Division=",div(a,b))
	else:
		print("Invalid choice...exit...")
		exit(0)
