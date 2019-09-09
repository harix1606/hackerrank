string = '1110011110001100010100000011011101100001101010001111101101000010111111001110110000010110010011100010'
string = list(string)

char={"010":"011"}

for index,item in enumerate(string):
    for key,value in char.items():
        if item[index:index+3]==key:
            string[index]=value

print("".join(string))

# def beautifulBinaryString(s):
# 	count = 0
# 	for i in range (0,len(s)-2):
# 		# reqd = s[i:i+3]
# 		# print (reqd)
# 		if (s[i:i+3] == '010'):
# 			s[i:i+3] = '011'
			
# 			count += 1
# 			print (s)
# 			print (i)

# 			# print (reqd)


# 	print (count)
# 	return count


# beautifulBinaryString(s)