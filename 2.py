def binary_search(array, target):
    low = 0
    high = len(array) - 1
    iter = 0

    while low <= high:
        center = (low + high) // 2
        iter += 1

        if array[center] < target:
            low = center + 1
        elif array[center] > target:
            high = center - 1
        else:
            return iter, array[center]

    if high >= 0:
        return iter, array[high]
    else:
        return iter, None

sorted = [0.1, 0.5, 0.7, 1.2, 1.5, 2.0, 2.5, 3.0, 3.5]
number = 1.3

searched = binary_search(sorted, number)

iteration = searched[0]
upper_number = searched[1]
print("Кількість ітерацій:", iteration)
if upper_number is not None:
    print("Верхня межа:", upper_number)
else:
    print("Елемент не знайдено. Верхня межа: ", sorted[-1])
