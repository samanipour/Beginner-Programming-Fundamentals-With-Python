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