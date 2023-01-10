# Определить самую высокую температуру и самый теплый день в мае.
from random import randint

days_in_may = [day for day in range(1, 32)]
temp_in_may = [randint(15, 23) for temp in range(1, 32)]
dict_temp = dict(zip(days_in_may, temp_in_may))
print(dict_temp)
print(f'{max(dict_temp.values())} градусов было {max(dict_temp, key=dict_temp.get)} числа')
