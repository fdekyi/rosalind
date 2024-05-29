input_string = input()

dictionary = {}

for sub_string in input_string.split(' '):
	count = 0

	if sub_string in dictionary:
		count = dictionary[sub_string]

	dictionary[sub_string] = count + 1

for key in dictionary:
	print(key + ' ' + str(dictionary[key]))