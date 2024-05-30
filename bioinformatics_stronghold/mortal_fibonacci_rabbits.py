from functools import reduce

user_input = [int(item) for item in input().split(' ')]
months = user_input[0]
longevity = user_input[1]

rabbit_pair_list = list(0 for index in range(0, longevity))
rabbit_pair_list[0] = 1

for month in range(2, months + 1):
    mature_pairs = 0
    for generation in reversed(range(0, len(rabbit_pair_list))):
        if generation > 0:
            mature_pairs += rabbit_pair_list[generation]

        if generation != len(rabbit_pair_list) - 1:
            rabbit_pair_list[generation + 1] = rabbit_pair_list[generation]

    rabbit_pair_list[0] = mature_pairs

print(str(reduce(lambda x, y: x + y, rabbit_pair_list)))