import sys

try:
    n = int(input('Enter Fibonacci number to calculate: '))
except ValueError:
    raise ValueError('Value is expected to be a number. Exiting...')
    sys.exit(1)

prev_number = 0
curr_number = 1

for index in range(curr_number, n):
    updated_curr_number = prev_number + curr_number
    prev_number = curr_number
    curr_number = updated_curr_number

print(curr_number)
