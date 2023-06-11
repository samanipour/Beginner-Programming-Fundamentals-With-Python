def main():
    def is_twin_pair(n):
        return is_prime(n) and is_prime(n + 2)
    def is_cousin_pair(n):
        return is_prime(n) and is_prime(n + 4)
    def is_sexy_pair(n):
        return is_prime(n) and is_prime(n + 6)
    # manual update
    twin_pairs = {}
    for i in range(1, 50):
        if is_twin_pair(i):
            twin_pairs.update({i: i + 2})
    # dict comprehensions
    cousin_pairs = {i: i + 4 for i in range(1, 50) if is_cousin_pair(i)}
    sexy_pairs = {i : i + 6 for i in range(1, 50) if is_sexy_pair(i)}
    print("Twins:", twin_pairs)
    print("Cousins:", cousin_pairs)
    print("Sexy:", sexy_pairs)
def is_prime(n):
    primes = calc_primes_up_to(n + 1)
    return n in primes

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