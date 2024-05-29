#install numpy
from math import floor

string  = input()
indices = [int(item) for item in input().split()]
output = []

for i in range(0, floor(len(indices) / 2)):
	start = indices[2 * i]
	end = indices[2 * i + 1]

	curr_string = ""

	for j in range(start, end + 1):
		curr_string += string[j]

	output.append(curr_string)

print(' '.join(output))