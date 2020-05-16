result = 2 ** 1000
result = str(result)
sum_digits = 0
for ch in result:
    sum_digits += int(ch)

print(sum_digits)
