def calc_armstrong_numbers():
    results = []
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                numeric_value = x * 100 + y * 10 + z
                cubic_value = int(pow(x, 3) + pow(y, 3) + pow(z, 3))
                if numeric_value == cubic_value:
                    results.append(numeric_value)
    return results