def parse_dna_string(dna_data):
	dna_data_lines = dna_data.split('\n')

	dna_data_label = dna_data_lines[0]
	dna_data_string = ""
	for index in range(1, len(dna_data_lines)):
		dna_data_string += dna_data_lines[index]

	return (dna_data_label, dna_data_string)


dataset_file = open("../resources/computing_gc_content_input.txt", "r")
dataset = dataset_file.read()
split_dataset = list(filter(lambda x: x != '', dataset.split('>')))

dna_strings = {}
for dna_string in split_dataset:
	(dna_data_label, dna_data_string) = parse_dna_string(dna_string)
	dna_strings[dna_data_label] = dna_data_string

highest_gc_content = ('', 0)
for key in dna_strings:
	gc_count = dna_strings[key].count('G') + dna_strings[key].count('C')
	gc_ratio = gc_count / len(dna_strings[key])
	if gc_ratio > highest_gc_content[1]:
		highest_gc_content = ( key, gc_ratio )

print(highest_gc_content[0])
print(highest_gc_content[1] * 100)