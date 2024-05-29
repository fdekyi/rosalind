from functools import reduce

dna_string = input()

nucleotides = [ 'A', 'C', 'G', 'T']
nucleotide_dictionary = { 'A': 0, 'C': 0, 'G': 0, 'T': 0 }

for index in range(0, len(dna_string)):
	if dna_string[index] in nucleotides:
		curr_nucleotide = dna_string[index]
		nucleotide_dictionary[curr_nucleotide] += 1

print(reduce(lambda x, value: x + " " + str(value), nucleotide_dictionary.values(), "").strip())