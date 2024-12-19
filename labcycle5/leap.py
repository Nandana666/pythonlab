import calendar
n=int(input("Enter a year:"))
s=calendar.isleap(n)
if(s==True):
	print(n," is a leap year")
else:
	print(n," is not a leap year")
