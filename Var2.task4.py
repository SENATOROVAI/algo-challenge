def sort_and_find_min_duplicates(arr):
    # Печатаем исходный список
    print("Исходный список:", arr)

    # Сортируем список
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    # Печатаем отсортированный список
    print("Отсортированный список:", arr)

    # Находим минимальное число, встречающееся более одного раза
    min_duplicate = float('inf')
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1] and arr[i] < min_duplicate:
            min_duplicate = arr[i]

    return min_duplicate

# Пример использования
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
result = sort_and_find_min_duplicates(arr)
print("Минимальное число, встречающееся более одного раза:", result)
