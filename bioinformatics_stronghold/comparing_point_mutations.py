dna_string_1 = input()
dna_string_2 = input()

hamming_distance = 0
for index in range(0, len(dna_string_1)):
	if dna_string_1[index] != dna_string_2[index]:
		hamming_distance += 1

print(hamming_distance)