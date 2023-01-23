# Функция find_athlets принимает 3 списка с именами студентов. В первом списке (know_english) — список тех, кто хорошо владеет английским языком.
# Второй (sportsmen) — содержит имена тех, кто увлекается спортом.
# Ну и третий (more_than_20_years) — предоставляет информацию о тех, кто старше 20 лет.
# Функция возвращает список имен студентов, которые подходят под все три критерия.

know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]


def find_athlets(list1, list2, list3):
    n = 0
    athlets_list = []
    while n < len(know_english):
        if know_english[n] in sportsmen and know_english[n] in more_than_20_years:
            athlets_list.append(know_english[n])
        n += 1
    return athlets_list


print(find_athlets(know_english, sportsmen, more_than_20_years))
