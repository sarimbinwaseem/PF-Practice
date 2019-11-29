def circlee(r):
	area = 3.142 * (r**2)
	peri = 2 * 3.142 * r
	# print(area)
	area = area + (area/100) * 5
	peri =  peri + (peri/100) * 5
	print("Area of Circle with 5% increment:",round(area,2))
	print("Perimeter of Circle with 5% increment:",round(peri,2))
circlee(56)