from palindrome import is_palindrome
def findlongest(s):
	longest=""
	for i in range(len(s)):
		for j in range(i+1,len(s)+1):
			substring=s[i:j]
			if is_palindrome(substring) and len(substring)>len(longest):
				longest=substring
	return longest
text=input("Enter a string:")
result=findlongest(text)
print("Longest palindrome substring:",result)

