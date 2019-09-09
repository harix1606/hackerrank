expenditure = [2,3,2,3,6,8,4,5]
d = 5

def counting_sort(array1):
    m = max(array1) + 1
    count = [0] * m                
    
    for a in array1:
    # count occurences
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    return array1

freqTable = {}

def median(array):
	exp_arr = counting_sort(array)

	for expenses in exp_arr:
		if (expenses in freqTable):
			freqTable[expenses] += 1
		else:
			freqTable[expenses] = 1

	print (freqTable)

	count = 0
	median  = 0
	median1 = 0
	median2 = 0
	num1 = 0
	num2 = 0

	for key,value in freqTable.items():

		if (len(array)%2 != 0):
			pos = int((len(array)/2)+1)
			if (count <= pos):
				count += value
				median = key
			else:
				break

		elif (len(array)%2 == 0):
			pos1 = int(len(array)/2)
			if (num1 <= pos1):
				num1 += value
				median1 = key
				print (median1, num1)
			else:
				break

			pos2 = pos1 + 1
			if (num2 <= pos2):
				num2 += value
				median2 = key
			else:
				break

			median = (median1+median2)/2
	
	# print (pos1,pos2)
	return median



a = median(expenditure)
print (a)			
