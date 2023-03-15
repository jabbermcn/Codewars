# Найди в словаре два самых больших значения и определи их ключи


d = {
    'a': 11,
    'q': 222,
    'c': 5,
    'd': 244,
}


def biggest_value(d: dict):
    sorted_values = sorted(d.items(), reverse=True, key=lambda x: x[1])[0:2]
    key = [k for k, v in sorted_values]
    return key


print(biggest_value(d))
