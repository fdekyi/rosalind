input_file = open('../resources/reading_and_writing_input.txt', 'r',)
lines = input_file.readlines()
output_text = ''
index = 1
for line in lines:
	if index % 2 == 0:
		output_text += line

	index += 1

output_file = open('../resources/reading_and_writing_output.txt', 'w')
output_file.write(output_text)