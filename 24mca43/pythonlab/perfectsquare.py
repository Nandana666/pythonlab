import math
def even_square(start,end):
	result=[]
	l_bound=math.ceil(math.sqrt(start))
	u_bound=math.floor(math.sqrt(end))
	for i in range(l_bound,u_bound+1):
		square=i**2
		if all(int(digit)%2==0 for digit in str(square)):
			result.append(square)
	return result
start_range=1000
end_range=9999
even_digit=even_square(start_range,end_range)
print("Four digit perfect squares with an even digits are:",even_digit)
