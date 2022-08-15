def move_zeros(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]


a = move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
print(a)
