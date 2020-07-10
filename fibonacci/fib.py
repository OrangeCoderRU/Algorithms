def fib_low(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_low(n - 1) + fib_low(n - 2)

print("Быстрый рекурсивный алгоритм:", fib_low(2))

# запоминаем все числа в списке
def fib(n):
    list = []
    for fib_num in range(n + 1):
        list.append(fib_num)
    for num in list:
        if num <= 1:
            pass
        else:
            list[num] = list[num - 1] + list[num - 2]
    # return  list[len(list) - 1] % 10
    return  list[len(list) - 1]


print("Обычные числа Фибоначчи:", fib(10))

# запоминаем  последние два
def fib_maxnum(n):
    list = [0, 1]
    for num in range(n):
        list.append(list[1] + list[0])
        list.pop(0)
    return list[0]

print("Относительно быстрый расчет большого числа:", fib_maxnum(100))

# запоминаем последние два и узнаем последнюю цифру числа n
def fib_max_last(n):
    list = [0, 1]
    for num in range(n):
        list.append((list[1] % 10) + (list[0] % 10))
        list.pop(0)
    return list[0] % 10

print("Последняя цифра большого числа Фибоначчи:", fib_max_last(696352))
