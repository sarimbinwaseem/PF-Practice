def rect(leng, bre):
	area = leng * bre
	peri = 2 * (leng + bre)
	# print(area)
	area = area + (area/100) * 8
	peri =  peri + (peri/100) * 8
	print("Area of Rectangle with 8% increment:",round(area,2))
	print("Perimeter of Rectangle with 8% increment:",round(peri,2))

rect(90, 56)