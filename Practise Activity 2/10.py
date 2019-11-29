def alpha(alph):
	leng = len(alph)
	alph = alph.lower()
	# print(alph)
	for a in "qwertyuioplkjhgfdsazxcvbnm":
		if a in alph:
			pass
		else:
			print("{} is missing".format(a))
	


alph = input("Enter string: ")
alpha(alph)