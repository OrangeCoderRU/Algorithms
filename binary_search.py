def binary_search(list, item):
    """Алгоритм бинарного поиска"""
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[int(mid)]
        if guess == item: # совпадение
            return mid
        if guess > item: # уменьшаем максимум наполовину
            high = mid - 1
        else: # увеличиваем минимум наполовину
            low = mid + 1
    return None

list = [5, 10, 15, 20, 25]

print(binary_search(list, 20)) # 3
