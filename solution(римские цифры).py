"""Переводим арабские числа в римские"""


def solution(n: int) -> str:
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]
    return thous[n // 1000] + hunds[n // 100 % 10] + tens[n // 10 % 10] + ones[n % 10]


a = solution(2020)
print(a, type(a))

"""Парсим римские числа, на ввод приходит римский символ"""
romans = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)


def parse_roman(roman):
    result = 0
    for i, c in enumerate(roman):
        if i + 1 < len(roman) and romans[i + 1] < romans[roman[i + 1]]:
            result -= roman[i + 1]
        else:
            result += roman[i + 1]
    return result
