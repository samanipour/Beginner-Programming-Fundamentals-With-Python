def calc_prime_factors(value):
    all_primes = calc_primes_up_to(value)
    prime_factors = []
    remaining_value = value
    # as long as even, divide by 2 again and again
    while remaining_value % 2 == 0 and remaining_value >= 2:
        remaining_value = remaining_value // 2
        prime_factors.append(2)
    # check remainder for prime
    if is_prime(all_primes, remaining_value):
        prime_factors.append(remaining_value)
    else:
    # remainder is not a prime number, further check
        while remaining_value > 1:
            for current_prime in all_primes:
                if remaining_value % current_prime == 0:
                    remaining_value = remaining_value // current_prime
                    prime_factors.append(current_prime)
                # start again from the beginning, because every divisor
                # may occur more than once
                    break
    return prime_factors

def is_prime(all_primes, n):
    return n in all_primes

def calc_primes_up_to(max_value):
    # initially mark all values as potential prime number
    is_potentially_prime = [True for _ in range(1, max_value + 2)]
    # run through all numbers starting at 2, optimization only up to half
    for number in range(2, max_value // 2 + 1):
        if is_potentially_prime[number]:
            erase_multiples_of_current(is_potentially_prime, number)
    return build_primes_list(is_potentially_prime)

def erase_multiples_of_current(values, number):
    for n in range(number + number, len(values), number):
        values[n] = False
    # print("Eliminating:", n)

def build_primes_list(is_potentially_prime):
    primes = []
    for number in range(2, len(is_potentially_prime)):
        if is_potentially_prime[number]:
            primes.append(number)
    return primes