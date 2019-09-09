def rotLeft(a,d):
	a2 = a[d:] + a[:d]
	print (a2)
	return a2

arr = [2,1,2,1,3,5,3,1]
rotLeft(arr,4)