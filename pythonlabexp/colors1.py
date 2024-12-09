color_list1=[]
color_list2=[]
n1=int(input("Enter no.of colors in first list:"))
print("List 1")
for i in range(n1):
	color=input("Enter color:")
	color_list1.append(color)
n2=int(input("Enter no.of colors in second list:"))
print("List 2")
for i in range(n2):
        color=input("Enter color:")
        color_list2.append(color)
result=[]
for color in color_list1:
	if color not in color_list2:
		result.append(color)
print("Colors from color_list1 not in color_list2:",result)
