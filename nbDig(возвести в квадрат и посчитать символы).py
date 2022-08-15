def nb_dig(n, d):
    sqrt = [str(i ** 2) for i in range(n+1)]
    sqrt_join = ''.join(sqrt)
    return sqrt_join.count(str(d))


a = nb_dig(5750, 0)
print(a)
