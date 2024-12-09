n=int(input("Enter the no.of words:"))
wordlist=[]
for i in range(n):
	word=input("Enter words:")
	wordlist.append(word)
max_length=0
for i in wordlist:
	if len(i)>max_length:
		max_length=len(i)
		word=i
print("Length of the longest word:",max_length)
print("Longest word:",word)
