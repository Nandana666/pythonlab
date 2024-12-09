import math
print(f"Quadratic equation ax^2+bx+c")
a=float(input("Enter a value for a:"))
b=float(input("Enter a value for b:"))
c=float(input("Enter a value for c:"))
num=(b*b)-(4*a*c)
if(num==0):
	print("Only one root is possible")
	ans=(-b)/2*a
	print(f"x1={ans}")
elif(num>0):
	sqrtvalue=math.sqrt(num)
	ans1=(-b+sqrtvalue)/2*a
	ans2=(-b-sqrtvalue)/2*a
	print("Roots are real")
	print(f"x1={ans1}")
	print(f"x2={ans2}")
else:
	print("Complex number")
	sqrtvalue=math.sqrt(abs(num))/2*a
	print(-b/(2*a),"+i",sqrtvalue)
	print(-b/(2*a),"-i",sqrtvalue)
	
