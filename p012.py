import math

def gen_divisors(number):
    divisors = []
    root = math.floor(math.sqrt(number))
    for i in range(1, root + 1):
        if number % i == 0:
            divisors.append(i)
            if i != root:
                divisors.append(number // i)
    return sorted(divisors)

num_divisors = 0
num = 0
addition = 1
while num_divisors < 500:
    num += addition
    num_divisors = len(gen_divisors(num))
    addition += 1

print(num)
