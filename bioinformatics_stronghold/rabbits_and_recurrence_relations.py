user_input = [int(item) for item in input().split()]

months = user_input[0]
litter_size = user_input[1]

mature_pairs = 0
immature_pairs = 1

for curr_month in range(1, months):
	maturing_pairs = immature_pairs
	immature_pairs = mature_pairs * litter_size
	mature_pairs += maturing_pairs

print(mature_pairs + immature_pairs)