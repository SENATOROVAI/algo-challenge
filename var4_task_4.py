"""Задание 4.
Напишите программу, которая сортирует
список, а затем находит
максимальное из тех чисел, 
что встречаются в массиве
три раза и более. Не использовать
встроенные функции"""


def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    
def max_three_times(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    sorted_keys = sorted(count_dict, key=lambda x: count_dict[x], reverse=True)
    
    for key in sorted_keys:
        if count_dict[key] >= 3:
            return key
    
    return None

# Пример использования
lst = [4, 2, 9, 3, 2, 7, 4, 9, 2, 3, 4, 4, 3]
sort_list(lst)
result = max_three_times(lst)
print(result) # Вывод: 4
