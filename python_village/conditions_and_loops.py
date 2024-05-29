user_input = [int(item) for item in input().split()]
output = 0

for i in range(user_input[0], user_input[1] + 1):
	if i % 2 == 1:
		output += i

print(output)