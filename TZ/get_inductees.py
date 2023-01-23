# Функция get_inductees принимает 3 списка одинаковой длины.
# В первом списке (names) — имена студентов, позволяющие их точно идентифицировать.
# Во втором (birthday_years) — год рождения. В третьем (genders) — пол студента.
# Частично они отсутствуют ввиду испорченного листа бумаги.
# Функция возвращает список с именами студентов мужского пола, которые достигли или могут
# достигнуть 18 лет в 2021 году, но при этом не старше 30 лет.
# Cтуденты, по которым невозможно точно установить - попадают они в список или нет (из-за порчи данных),
# должны быть выведены отдельно.

names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo", "Mark2", "Mark3", "Mark4"]
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001, 2000, 2001, 2002]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None, "Male", "Male", "Female"]


def get_inductees(list1: list, list2: list, list3: list):
    liable_for_military_service = list(zip(list1, list2, list3))
    may_be_called = []
    not_enough_information = []
    for items in liable_for_military_service:
        if items[1] is not None and items[2] is not None and items[2] != 'Female':
            current_age = 2021 - items[1]
            if 18 <= current_age <= 30:
                may_be_called.append(items[0])
        elif items[2] != 'Female':
            not_enough_information.append(items[0])
    return f'Могут быть призваны: {may_be_called}. Не достаточно информации: {not_enough_information}'


print(get_inductees(names, birthday_years, genders))
