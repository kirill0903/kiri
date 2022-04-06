def sum_numbers(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))

print(sum_numbers(2,6))