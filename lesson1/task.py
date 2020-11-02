sequences = [10, 345, 2, 1, 43, 2, 5, 2, 1, 7, 3, 25, 7, 4]

# TODO element > 4 power 2

# filter(lambda number: number > 4, sequences)


ptr_next = map(lambda number: number*number, filter(lambda number: number > 4, sequences))

print(list(ptr_next))