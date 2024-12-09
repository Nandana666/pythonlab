numbers=[-70,15,8,3,4,-9,0,-3]
positive_numbers=[num for num in numbers if num>0]
print("Positive numbers:",positive_numbers)
N=5
squares=[num**2 for num in range(1,N+1)]
print("Squares of first N numbers:",squares)
word="helloworld"
vowels=[char for char in word if char in 'aeiou']
print("Vowels of the word:",vowels)
word="hello"
ordinal_value=[ord(char) for char in word]
print("Ordinal values of each character:",ordinal_value)

