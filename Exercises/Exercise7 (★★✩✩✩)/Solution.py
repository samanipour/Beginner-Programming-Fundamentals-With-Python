def calc_checksum(digits):
    if not digits.isdigit():
        raise ValueError("illegal chars: not only digits")
    crc = 0
    for i, current_char in enumerate(digits):
        value = (int(current_char)) * (i + 1)
        crc += value
    return int(crc % 10)