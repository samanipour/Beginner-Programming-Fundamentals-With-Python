def calc(m, n):
    # Solution 1
    return m * n // 2 % 7

def calc_v2(m, n):
    # Solution 2
    return int(m * n / 2) % 7