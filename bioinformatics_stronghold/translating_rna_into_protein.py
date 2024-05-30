from utils.rna_codon_dictionary import get_rna_codon_dictionary
import re as regex

rna_string = input()
print(rna_string)
codon_list = regex.findall(r'\w{3}', rna_string)

rna_codon_dictionary = get_rna_codon_dictionary()
translated_protein = ''

for codon in codon_list:
    amino_acid_string = rna_codon_dictionary[codon]
    if amino_acid_string == 'Stop':
        break

    translated_protein += amino_acid_string


output_file = open('../resources/translating_rna_into_protein_output.txt', 'w')
output_file.write(translated_protein)
print('File has been written to: /resources/translating_rna_into_protein_output')