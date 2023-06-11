def from_roman_number(roman_number):
    value_map = {"I": 1, "V": 5, "X": 10, "L": 50,"C": 100, "D": 500, "M": 1000}
    value = 0
    last_digit_value = 0
    # for i in range(len(roman_number) - 1, -1, -1):
    # roman_digit = roman_number[i]
    for roman_digit in reversed(roman_number):
        digit_value = value_map[roman_digit]
        add_mode = digit_value >= last_digit_value
    if add_mode:
        value += digit_value
        last_digit_value = digit_value
    else:
        value -= digit_value
    return value
