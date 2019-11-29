def sep(lis):
	even = []
	odd = []
	for p in lis:
		if int(p)%2 == 0:
			even.append(p)
		else:
			odd.append(p)
	print("Even numbers: ",end="")
	for p in sorted(even):
		print(p, end=" ")
	print()
	print("Odd numbers: ",end="")
	for p in sorted(odd):
		print(p, end=" ")
	print()

lis = "78644468566591354868549873654752484653457826"
sep(lis)
