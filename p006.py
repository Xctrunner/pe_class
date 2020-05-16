sum_squares = sum([(x + 1) ** 2 for x in range(100)])
square_sums = sum([x + 1 for x in range(100)]) ** 2

print(square_sums - sum_squares)
