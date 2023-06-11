def is_perfect_number_simple(number):
# always divisible by 1
    sum_of_multipliers = 1
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            sum_of_multipliers += i
    return sum_of_multipliers == number

def calc_perfect_numbers(max_exclusive):
    results = []
    for i in range(2, max_exclusive):
        if is_perfect_number_simple(i):
            results.append(i)
    return results