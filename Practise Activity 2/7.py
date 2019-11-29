def vow_count(opi):
	vow = 0
	length = len(opi)
	for o in opi:
		if o in "aeiouAEIOU":
			vow += 1
		else:
			pass
	conso = length - vow
	print("Number of vowels are {} and number of consonants are {}.".format(vow, conso))

opi = input("Enter string to count vowels and consonants: ")
vow_count(opi)