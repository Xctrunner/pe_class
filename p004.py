def is_num_palindrome(number):
    return str(number) == str(number)[::-1]


highest = 0
iterations = 0
for i in range(999, 99, -1):
    iterations += 1
    for j in range(999, i - 1, -1):
        candidate = i * j
        if is_num_palindrome(candidate) and candidate > highest:
            highest = candidate
            iterations = 0
    if iterations > 100:
        break


print(highest)
