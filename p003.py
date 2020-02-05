import math
from utils import gen_primes


def get_prime_factors(number):
    # root = math.floor(math.sqrt(number))
    primes_up_to_number = gen_primes(number)
    prime_factors = []
    for prime in primes_up_to_number:
        if number % prime == 0:
            prime_factors.append(prime)
    return sorted(prime_factors)


def get_prime_factors_2(number):
    primes = [2]
    factors = []
    test_val = 3
    while test_val < math.sqrt(number):
        val_prime = True
        for k in primes:
            if test_val % k == 0:
                val_prime = False
                test_val += 2
        if val_prime:
            primes.append(test_val)
            if number % test_val == 0:
                factors.append(test_val)
                number //= test_val
    factors.append(number)
    return factors


print(get_prime_factors_2(600851475143))
