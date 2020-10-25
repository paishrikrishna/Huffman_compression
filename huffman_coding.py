

msg = list(input("Enter your msg "))
ltr , co = [],[]
for i in msg:
	if i not in ltr:
		ltr.append(i)
		co.append(msg.count(i))
#print(co,ltr)
for i in range(len(co)):
	f = 0
	for j in range(len(co)-i-1):
		if (co[j] > co[j+1]):
			f = 1
			co[j] , co[j+1] = co[j+1] , co[j]
			ltr[j] , ltr[j+1] = ltr[j+1] , ltr[j]
	
	if f == 0:
		break
	

#print(co,ltr)
t = []
for i in range(len(co)):
	t.append([ltr[i],0b0])


print("tree")
print("\n")
print(co,ltr)

while len(ltr) > 1:
	f1 = min(co)
	index1 = co.index(f1)
	c1 = ltr[index1]
	co[index1] = max(co) * 100
	for i in range(len(co)):
		if co[i] == min(co) and i != index1:
			f2 = co[i]
			index2 = i
			c2 = ltr[i]
			break


	if index1 < index2:
		ltr.pop(index2)
		ltr.pop(index1)
		co.pop(index2)
		co.pop(index1)
		index = index1
		for i in range(len(t)):
			if t[i][0] == c1:
				t[i][1] = 0b0;
				break


		for i in range(len(t)):
			if t[i][0] == c2:
				t[i][1] = 0b1;
				break
	
	elif index1 > index2:
		ltr.pop(index1)
		ltr.pop(index2)
		co.pop(index1)
		co.pop(index2)
		index = index2
		for i in range(len(t)):
			if t[i][0] == c2:
				t[i][1] = 0b0;
				break
		

		for i in range(len(t)):
			if t[i][0] == c1:
				t[i][1] = 0b1;
				break
	
	
	
	co.insert(index,f1+f2)
	ltr.insert(index,c1+c2)
	t.append([c1+c2,0b0])
	print(co,ltr)

print("\n")
print("hauffman equivalent : ")	
print("\n")

t[-1][1]=2

#for i in range(len(t)):
#	print(t[-1-i])

di = {}
for i in msg:
	en=[]
	for j in range(len(t)):
		if ( i in list(t[-1-j][0]) ) and ( t[-1-j][1] != 2):
			en.append(str(t[-1-j][1]))
	di[i] = "".join(en)
	#print(i + " : " + en)

#print("".join(en))	
encoded_text = ""
for i in msg:
	encoded_text += di[i]

# padded text

extra_padding = 8 - len(encoded_text) % 8
for i in range(extra_padding):
	encoded_text += "0"
padded_info = "{0:08b}".format(extra_padding)
padded_encoded_text = padded_info + encoded_text

b = bytearray()
for i in range(0,len(padded_encoded_text),8):
	byte = padded_encoded_text[i:i+8]
	b.append(int(byte,2))
#print(bytes(b))
file = open('read.bin', 'wb') 
file.write(bytes(b)) 
file.close() 

