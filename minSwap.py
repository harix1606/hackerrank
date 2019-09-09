sample = [4,3,1,2]

swaps = 0
def minimumSwaps(arr):
	for i in range (len(arr)):
		if (arr[i] != i+1):			
			arr[arr[i]-1],arr[i] = arr[i], arr[arr[i]-1]
			global swaps
			swaps += 1

	sr = sorted (arr)
	while (sr != arr):
		minimumSwaps(arr)
	
	return swaps


a =minimumSwaps(sample)
print (a)

