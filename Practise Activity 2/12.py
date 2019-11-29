def far(r1, r2):
	a1 = 3.142 * (r1**2)
	a2 = 3.142 * (r2**2)

	a = abs(a1 - a2)
	print("Remaining area of circle is:", a)

r1 = input("Enter radius of first circle: ")
r2 = input("Enter radius of second circle: ")

far(r1, r2)