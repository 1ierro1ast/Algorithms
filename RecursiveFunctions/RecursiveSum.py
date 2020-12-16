def sum(l):
	if len(l) > 0:
		return l[0] + sum(l[1:])
	else:
		return 0