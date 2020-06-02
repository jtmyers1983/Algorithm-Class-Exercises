def freq(a_string):
	f = [None]
	# do the computation here...
	for c in a_string:
		if c not in f:
			f[c] = 1
		else:
			f[c] = f[c] + 1
	return f 

print(freq([1,2,3,4,3,2,3]))