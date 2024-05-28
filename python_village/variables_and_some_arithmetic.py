from math import pow, trunc

triangle_sides = [ 952, 967 ]
hypotenuse_squared = 0

for side in triangle_sides:
    hypotenuse_squared += pow(side, 2)

print(trunc(hypotenuse_squared))