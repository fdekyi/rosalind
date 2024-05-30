def parse_dna_string(dna_data):
	dna_data_lines = dna_data.split('\n')

	dna_data_label = dna_data_lines[0]
	dna_data_string = ""
	for index in range(1, len(dna_data_lines)):
		dna_data_string += dna_data_lines[index]

	return (dna_data_label, dna_data_string)

dataset_file = open("../resources/consensus_and_profile_input.txt", "r")
dataset = dataset_file.read()
split_dataset = list(filter(lambda x: x != '', dataset.split('>')))

dna_strings = {}
dna_string_length = 0
for dna_string in split_dataset:
    (dna_data_label, dna_data_string) = parse_dna_string(dna_string)
    dna_strings[dna_data_label] = dna_data_string
    dna_string_length = len(dna_data_string)

profile_matrix = {
    'A': [0 for index in range(0, dna_string_length)],
    'C': [0 for index in range(0, dna_string_length)],
    'G': [0 for index in range(0, dna_string_length)],
    'T': [0 for index in range(0, dna_string_length)],
}

common_ancestor_string = ''

for index in range(0, dna_string_length):
    max_count = 0
    common_ancestor_base = ''
    for dna_string in dna_strings.values():
        profile_matrix[dna_string[index]][index] += 1

        if profile_matrix[dna_string[index]][index] > max_count:
            max_count =  profile_matrix[dna_string[index]][index]
            common_ancestor_base = dna_string[index]

    common_ancestor_string += common_ancestor_base

print(common_ancestor_string)
print('\n'.join(base + ': ' + ' '.join(map(str, profile_matrix[base])) for base in profile_matrix))


