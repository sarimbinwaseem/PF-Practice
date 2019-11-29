def sortnum(lis):
	# lis = int(lis)
	lis = sorted(lis)
	for i in lis:	
		print(i, end=" ")


lis = []
lis = input("Enter numbers: ")
sortnum(lis)