n=int(input("Enter n:"))
def prime(n):
	flag=0
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return false
	return true
def print(n):

	prime=[]
	for i in range(2,n+1):
		if prime(i):
			prime.append(i)
	alt_prime=prime[::2]
	return alt_prime
print("Alternate prime numbers are:",alt_prime)
