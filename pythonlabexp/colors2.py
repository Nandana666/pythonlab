color=input("Enter list of colors:")
colorlist=color.split(",")
for i in range(0,len(colorlist)):
	colorlist[i]=colorlist[i].replace("","")
	print(colorlist[i])
print("First color:",colorlist[0])
print("Last color:",colorlist[-1])
