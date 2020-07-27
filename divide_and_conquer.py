"""Разделяй и влавстуй, алгоритм нахождения суммы чисел"""
def sum(list):
    num = 0

    if len(list) == 1:
        """Наблюдаем алгоритм"""
        print(list, "- базовый случай")
    else:
        print(list)

    if len(list) == 0:
        """Сама функция"""
        return 0
    else:
        num = list[0] + sum(list[1:])
    return num

print("Ответ -", sum([2, 4, 6]))
