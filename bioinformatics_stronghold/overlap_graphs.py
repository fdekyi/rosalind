def parse_dna_string(dna_data):
	dna_data_lines = dna_data.split('\n')

	dna_data_label = dna_data_lines[0]
	dna_data_string = ""
	for index in range(1, len(dna_data_lines)):
		dna_data_string += dna_data_lines[index]

	return (dna_data_label, dna_data_string)

dataset_file = open("../resources/overlap_graphs_input.txt", "r")
dataset = dataset_file.read()
split_dataset = list(filter(lambda x: x != '', dataset.split('>')))

dna_strings = {}
dna_string_length = 0
x_fix_length = 3
adjacency_list = set()
for dna_string in split_dataset:
    (dna_data_label, dna_data_string) = parse_dna_string(dna_string)
    dna_strings[dna_data_label] = dna_data_string
    dna_string_length = len(dna_data_string)

for dna_string_a in dna_strings:
    prefix = dna_strings[dna_string_a][0:x_fix_length]
    for dna_string_b in dna_strings:
        if dna_string_a == dna_string_b or dna_strings[dna_string_a] == dna_strings[dna_string_b]:
            continue

        current_string = dna_strings[dna_string_b]
        suffix = current_string[len(current_string) - x_fix_length: len(current_string)]
        if prefix == suffix:
            if dna_string_a < dna_string_b:
                adjacency_list.add(dna_string_a + ' ' + dna_string_b)
            else:
                adjacency_list.add(dna_string_b + ' ' + dna_string_a)

print('\n'.join(adjacency_list))