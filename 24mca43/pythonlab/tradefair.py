age=int(input("Enter your age:"))
if age<10:
	print("Your ticket rate is:7")
elif 10<=age<60:
	print("Your ticket rate is:10")
elif age>=60:
	print("Your ticket rate is:5")
else:
	print("Enter the proper age")
