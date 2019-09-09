arr = [[2,1,2,1,0,2],[1,2,0,2,0,3],[0,1,1,2,1,1],[2,2,2,0,0,0],[1,1,0,0,1,2],[2,2,0,1,0,0]]

def hourglassSum(arr):
	hourglassSum = -100
	for i in range(0,4):
		for j in range(0,4):
			a = arr[i][j:j+3]
			a.append(arr[i+1][j+1])
			fin = a + arr[i+2][j:j+3]
			print (sum(fin))
			if (sum(fin)>hourglassSum):
				hourglassSum = sum(fin)

	return hourglassSum

array = []

for i in range(0,6):
	l = list(map(int,input().split()))
	array.append(l)

ans = hourglassSum(array)
print (ans)

# a = [-1,-3,-2,-3,-1]
# print (sum(a))