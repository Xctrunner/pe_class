from utils import gen_primes


prime_list = []
limit = 10000
while len(prime_list) < 10001:
    prime_list = gen_primes(limit)
    limit *= 10

print(prime_list[10000])
