def verb_cont(verbs):
	verbs = verbs.split()
	for v in verbs:
		v = v + "ing"
		print(v)



verbs = input("Enter verbs to be converted to continous by giving space between them: ")
verb_cont(verbs)