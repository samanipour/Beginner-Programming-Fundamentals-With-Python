def calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive):
    count = 0
    sum = 0
    for i in range(1, max_exclusive):
        if i % 2 == 0 or i % 7 == 0:
            count += 1
            sum += i
    print("count:", count)
    print("sum:", sum)