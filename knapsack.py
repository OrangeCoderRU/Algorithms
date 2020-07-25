"""Задача о непрерывном рюкзаке"""
n, w = map(float, input().split())
w_current = 0
c_current = 0
list_items = []
while n > len(list_items):
    """Добавляем предметы"""
    item = input()
    list_items.append(item.split())

def funcsort(x):
    """Сортируем по убыванию стоимости"""
    return int(x[0]) / int(x[1])

list_items = sorted(list_items, key=funcsort, reverse=True)
print(list_items)

for item in list_items:
    """Удостоверяемся в убывании стоимости"""
    print("C/W предмета №", list_items.index(item), "-", funcsort(item))

for item in list_items:
    """Смотрим предметы в порядке убывания стоимости"""
    if w_current + float(item[1]) < w:
         """Предмет помещяется полностью - добавляем"""
         c_current += float(item[0])
         w_current += float(item[1])
         print("с =", c_current, "w =", w_current)
    elif w_current + float(item[1]) >= w:
        """Делим на части и добавляем по килограмму"""
        for num in range(int(item[1])):
            if int(w_current) == int(w):
                break
            c_current += float(item[0]) / float(item[1])
            w_current += 1
            print("Итерация -", num, "с =", c_current, "w =", w_current)

print('{:.3f}'.format(c_current), w_current)
