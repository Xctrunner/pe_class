def gen_fib(upper_limit):
    fib_1 = 1
    fib_2 = 2
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


fib_sum = sum(filter(lambda x: x % 2 == 0, gen_fib(4000000)))
print(fib_sum)
