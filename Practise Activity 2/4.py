def addeven(r):
	summ = 0
	for u in r:
		if int(u)%2 == 0:
			summ += int(u)
		else:
			pass
	if summ:
		print("Sum of even numbers in the string is:", summ)
	else:
		print("No number was even in the given string")

r = input("Enter numbers: ")
addeven(r)