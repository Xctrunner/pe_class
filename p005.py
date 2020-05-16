nums = [i for i in range(11, 21)]
product = 1
for i in nums:
    product *= i
product //= 16
product //= 15
product //= 12
print(product)
