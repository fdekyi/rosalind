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
dna_string_labels = []
x_fix_length = 3
adjacency_list = set()
for dna_string in split_dataset:
    (dna_data_label, dna_data_string) = parse_dna_string(dna_string)
    dna_strings[dna_data_label] = dna_data_string
    dna_string_labels.append(dna_data_label)

for dna_string_a in dna_string_labels:
    current_string = dna_strings[dna_string_a]
    suffix = current_string[len(current_string) - x_fix_length: len(current_string)]
    for dna_string_b in dna_string_labels:
        if dna_string_a == dna_string_b or dna_strings[dna_string_a] == dna_strings[dna_string_b]:
            continue

        prefix = dna_strings[dna_string_b][0:x_fix_length]
        if prefix == suffix:
            adjacency_list.add(dna_string_a + ' ' + dna_string_b)

print('\n'.join(adjacency_list))