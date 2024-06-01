from math import floor

search_file = open("../resources/binary_search_input.txt", "r")
array_length_a = int(search_file.readline())
array_length_b = int(search_file.readline())
array_a = [int(item) for item in search_file.readline().split()]
array_b = [int(item) for item in search_file.readline().split()]

def binary_search(search_list, value):
    if len(search_list) == 0:
        return -1
    if len(search_list) == 1:
        return 1 if search_list[0] == value else -1

    center = floor(len(search_list) / 2)
    if search_list[center] == value:
        return center + 1
    elif search_list[center] > value:
        return binary_search(search_list[0:center], value)
    else:
        index = binary_search(search_list[center:len(search_list)], value)
        return -1 if index == -1 else center + index

indexes = []    
for item in array_b:
    found_index = binary_search(array_a, item)
    indexes.append(found_index)

print(' '.join(map(str, indexes)))