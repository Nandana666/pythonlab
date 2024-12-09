def fibonacci(n):
	if n<=1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)
limit=int(input("Enter no.of terms:"))
if limit<=0:
	print("Please enter a positive integer")
else:
	print("Fibonacci series:")
	for i in range(limit):
		print(fibonacci(i))
