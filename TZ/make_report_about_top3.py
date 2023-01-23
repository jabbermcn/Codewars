import pandas as pd

# Функция make_report_about_top3 принимает словарь (students_avg_scores), в котором ключами являются имена студентов,
# а значениями — средний балл за всю учебу. Функция находит ТОП-3 студентов, чей средний балл выше, чем у других.
# Функция возвращает ссылку на эксель-файл, в котором упомянуты 3 студента и который потом будет передан в бухгалтерию.
# Сам файл необходимо создать внутри функции. Важно сохранить совместимость с Excel, чтобы Ольга Петровна смогла без проблем получить всю нужную информацию.

students_avg_scores = {
    'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973,
    'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937, 'Mark2': 5,
}


def make_report_about_top3(some_dict: dict):
    top3_student = sorted(some_dict.values(), reverse=True)[0:3]
    name_of_top3 = []
    for k, v in some_dict.items():
        if v in top3_student:
            name_of_top3.append(k)
    df = pd.DataFrame({'name': name_of_top3})
    df.to_excel('/Users/mikhailouski_n/PycharmProjects/Codewars/TZ/TZ.xlsx')
    return name_of_top3


print(make_report_about_top3(students_avg_scores))
