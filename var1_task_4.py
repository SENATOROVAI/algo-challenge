"""
Напишите программу, которая сортирует список, а затем
находит максимальное из тех чисел, что встречаются в
 массиве три раза и более. Не использовать встроенные функции.
"""

# Tatiana
# ввод списка
# arr_1:list[int] = list(map(int, input().split())) # crate a list of numbers

arr_1 = [45, 7, 1, 3, 78, 3, 74, 3, 8, 7, 9, 3, 7, 48, 7, 5]

# пузырьковая сортировка
def bubble_sort(nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(
            len(nums) - 1
        ):  # задаем индексы от 0 до предпоследнего для спсика nums
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True

# сортировка списка
bubble_sort(arr_1) 
# print(arr_1)

# поиск максимальноего элемента повторяющегося >3 раз
max_number = 0
for i in range(len(arr_1) - 2):
    if arr_1[i] == arr_1[i + 1] == arr_1[i + 2] and max_number < arr_1[i]:
        max_number = arr_1[i]

print(max_number)

# Влад
# O(N**2)
numbers = list(map(int, input().split()))
for start in range(len(numbers)):
    for cont in range(start + 1, len(numbers)):
        if numbers[start] > numbers[cont]:
            first_number = numbers[start]
            second_number = numbers[cont]
            numbers[cont], numbers[cont] = second_number, first_number

maximum_search = [elem for elem in numbers if numbers.count(elem) >= 3]
try:
    print(maximum_search[-1])
except IndexError:
    print("Сheck the data is correct")
# .\Влад
