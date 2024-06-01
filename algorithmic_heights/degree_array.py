degree_file = open("../resources/degree_array_input.txt", "r")

vertex_array = []
degree_array_data = [int(item) for item in degree_file.readline().split()]
degree_array = [0 for index in range(0, degree_array_data[0])]

while current_line := degree_file.readline():
    # vertex_array.append([int(item) for item in current_line.split()])
    vertex_data = [int(item) for item in current_line.split()]
    degree_array[vertex_data[0] - 1] += 1
    degree_array[vertex_data[1] - 1] += 1
    
print(' '.join(map(str, degree_array)))