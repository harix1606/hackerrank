def countSort(array):

	s_ar = array
	m = max(s_ar) + 1
	count = [0] * m                
	
	for a in s_ar:
	# count occurences
		count[a] += 1

	i = 0
	for a in range(m):            
		for c in range(count[a]):  
			s_ar[i] = a
			i += 1
	return s_ar

def minimumBribes(q):
	bribes = 0
	for fp in range (len(q)):
		posit = q[fp] - 1

		if (fp < posit and posit-fp <= 2):
			bribes += posit-fp
			print (bribes)

		elif (fp < posit and posit-fp > 2):
			print ('Too chaotic')
			return "Too chaotic"
			break

	print (bribes)
	return bribes

minimumBribes([1,2,5,3,7,8,6,4])
