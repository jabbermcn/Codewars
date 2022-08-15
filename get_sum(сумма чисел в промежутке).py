def get_sum(a, b):
    sum_get = sum([i for i in range(min(a, b), max(a, b) + 1)])
    return sum_get


new_sum = get_sum(0, -1)
print(new_sum)
