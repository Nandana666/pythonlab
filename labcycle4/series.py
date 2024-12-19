import math
def factorial(n):
	return math.factorial(n)
def nth_term(n):
	return n**3/factorial(n)
def series_sum(n):
	sum=0
	for i in range(1,n+1):
		sum+=nth_term(i)
	return sum
n=int(input("Enter the number of terms:"))
print("Sum of the series:",series_sum(n))
