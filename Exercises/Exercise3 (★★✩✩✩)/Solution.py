def number_as_text(n):
    value = ""
    remaining_value = n
    while remaining_value > 0:
        remainder_as_text = digit_as_text(remaining_value % 10)
        remaining_value = int(remaining_value / 10)
        value = remainder_as_text + " " + value
    return value.strip()


def digit_as_text(n):
    value_to_text_mapping = { 0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE" }
    return value_to_text_mapping[n % 10]