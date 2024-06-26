# Find all prime numbers from 2 to 50.
print("Find all prime numbers from 2 to 50: ")
list= [2]
for i in range(3, 51):
	if (i > 10) and (i%10==5):
		continue
	for j in list:
		if j*j-1 > i:
			list.append(i)
			break
		if (i % j == 0):
			break
	else:
		list.append(i)
print(list)