def fib_mod(n, m):
    list = []
    period = []
    period_flag = False
    for fib_num in range((6 * m)):
        # считаем числа до 6m
        list.append(fib_num)
    for num in list:
        # превращаем числа в числа Фибоначчи и делим их на m
        if num <= 1:
            pass
        else:
            list[num] = (list[num - 1] + list[num - 2]) % m
    for per in list:
        # определяем период если он есть
        period.append(per)
        if period[len(period) - 1] == 0 and period[len(period) - 2] == 1:
            period.pop(len(period) - 1)
            period_flag = True
            break
    print("Лист остатков - ", list)
    if period_flag == True:
        print("Период Пизано для m =", m, ", числа Фибоначчи от i -", n, "равен -", period)
        print("Период длинной или (П(m)) -", len(period))
        print("Значит Mod", m, "от", n, "будет =", period[n % len(period)])
    else:
    # если периода нет, то берём остаток из списка
        print(list[n])

fib_mod(55,4)
