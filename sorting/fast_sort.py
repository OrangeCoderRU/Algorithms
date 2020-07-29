def quicksort(array):
    if len(array) < 2:
        """Базовый случай"""
        return array
    else:
        pivot = array[0] # опороный элемент
        # подмассив элементов меньше опорного
        less = [i for i in array[1:] if i <= pivot]
        # подмассив элементов больше опорного
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))
