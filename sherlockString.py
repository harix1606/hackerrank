import re
def allSame (array):
	for i in range (len(array)-1):
		if (array[i] != array[i+1]):
			return False
		else:
			return True

def isValid(s):
	strdict = {}
	for i in range (len(s)):
		strdict[s[i]] = len(re.findall(s[i],s))


	print (strdict)

isValid('appleban')	