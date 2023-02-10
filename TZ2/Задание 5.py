# Напиши функцию на Python, выполняющую сравнение версий.
# Условия:
# - Return -1 if version A is older than version B;
# - Return 0 if versions A and B equivalent;
# - Return 1 if version A is newer than version B;
# - Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1.


def version_compare(a, b):
    a = [int(i) for i in a.split('.')]
    b = [int(i) for i in b.split('.')]
    length = min(len(a), len(b))
    for i in range(length):
        if a[i] > b[i]:
            return 1
        elif a[i] < b[i]:
            return -1
    if len(a) > len(b):
        return 1
    elif len(a) < len(b):
        return -1
    else:
        return 0


print(version_compare('1.11', '1.2'))
