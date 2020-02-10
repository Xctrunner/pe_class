import math


def gen_primes(upper_limit):
    bool_list = [True for _ in range(upper_limit)]
    bool_list[0] = False
    root = math.floor(math.sqrt(upper_limit))
    for i in range(2, root + 1):
        if bool_list[i - 1]:
            square_list = [i ** 2 + x * i for x in range(upper_limit // i)]
            for j in square_list:
                if j - 1 < len(bool_list):
                    bool_list[j - 1] = False
    prime_list = []
    for x in range(len(bool_list)):
        if bool_list[x]:
            prime_list.append(x + 1)
    return prime_list

def gen_fib(upper_limit):
    fib_1 = 1
    fib_2 = 1
    fib_list = [fib_1, fib_2]
    fib_result = 0
    while True:
        fib_result = fib_1 + fib_2
        if fib_result > upper_limit:
            break
        else:
            fib_list.append(fib_result)
            fib_1 = fib_2
            fib_2 = fib_result
    return fib_list
