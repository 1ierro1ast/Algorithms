def length(l):
	if len(l) > 0:
		return 1 + len(l[1:])
	else:
		return 0