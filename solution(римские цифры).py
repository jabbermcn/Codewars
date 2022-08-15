def solution(n: int) -> str:
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]
    return thous[n // 1000] + hunds[n // 100 % 10] + tens[n // 10 % 10] + ones[n % 10]


a = solution(2020)
print(a, type(a))
