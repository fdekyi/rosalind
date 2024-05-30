dna_string = input()
dna_substring = input()

substring_positions = set()

for index in range(0, len(dna_string) - len(dna_substring) + 1):
    try:
        position = dna_string.index(dna_substring, index)
    except ValueError:
        position = -1

    if position != -1:
        substring_positions.add(position + 1)

print(' '.join(map(str, sorted(list(substring_positions)))))

