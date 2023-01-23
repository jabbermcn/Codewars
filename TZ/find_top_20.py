# Функция принимает на вход список сводной информации по абитуриентам (candidates)
# и возвращает список с  именами 20 человек, набравших наибольшее СУММАРНОЕ количество баллов
# (с учетом extra баллов), которые станут студентами университета.


candidates = [
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 33, "russian_language": 44, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 77, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 44, "computer_science": 34}, "extra_scores": 1},
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 55, "computer_science": 99}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 55, "russian_language": 85, "computer_science": 99}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 88}, "extra_scores": 1},
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 77}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 65, "russian_language": 85, "computer_science": 66}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 55}, "extra_scores": 1},
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 88, "computer_science": 44}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 33, "russian_language": 85, "computer_science": 33}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 22}, "extra_scores": 1},
    {"name": "Vasya", "scores": {"math": 85, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 33, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 69, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 55}, "extra_scores": 1},
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 23, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 33, "russian_language": 99, "computer_science": 66}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 77}, "extra_scores": 1},
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 88}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 67, "russian_language": 85, "computer_science": 99}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 44, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 22, "russian_language": 22, "computer_science": 34}, "extra_scores": 1},
]


def find_top_20(candidates_list: list) -> list:
    best_students_list = []
    for dicts in candidates_list:
        points = sum(dicts['scores'].values()) + dicts['extra_scores']
        best_students_list.append((dicts["name"], points))
    return sorted(best_students_list, key=lambda tup: tup[1], reverse=True)[0:20]


print(find_top_20(candidates))
