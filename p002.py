from utils import gen_fib

fib_sum = sum(filter(lambda x: x % 2 == 0, gen_fib(4000000)))
print(fib_sum)
