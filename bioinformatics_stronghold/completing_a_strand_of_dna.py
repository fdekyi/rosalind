dna_string = input()
complement_string = ""

look_up = { "A": "T", "T": "A", "G": "C", "C": "G" }

for index in range(0, len(dna_string)):
	if dna_string[index] in look_up:
		curr_base = dna_string[index]
		complement_string = look_up[curr_base] + complement_string

print(complement_string)
	