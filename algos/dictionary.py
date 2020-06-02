#goal: Learn about dictionaries

ages = {'thomas': 18}
print(type(ages))

ages['John'] = 23
ages['Mary'] = 22

for key in ages:
	print(key, ages[key])


table = {}
table[('john', 'memphis')] = 23
table[('john', 'nyc')] = 21

for key in table:
	print(key, table[key])


myFile = open('sumList.py')
for line in myFile:
	print(line.strip())
