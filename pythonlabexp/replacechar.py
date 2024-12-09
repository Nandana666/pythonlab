s=input("Enter your string:")
f=s[0]
newstr=f+s[1:].replace(f,'$')
print(f"{newstr}")
