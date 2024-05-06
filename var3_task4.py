"""Дан список. Назовем серией группу подряд идущих
 одинаковых элементов, а длиной серии
— количество этих элементов. Отсортировать список
 и сформировать два новых массива, в
один из них записывать длины всех серий,
а во второй — значения элементов, образующих
эти серии. Например, если исходный
список [3, 5, 1, 3, 5, 3] то элементы, создающие серии,
это [3, 5], а длины серий - [3,2].
Не использовать встроенные функции.
Файл с заданием: task_4.1.py"""


def sort_and_split_list(lst):
    sorted_lst = sorted(lst)
    lengths = []
    values = []
    current_length = 1
    current_value = sorted_lst[0]
    for i in range(1, len(sorted_lst)):
        if sorted_lst[i] == current_value:
            current_length += 1
        else:
            lengths.append(current_length)
            values.append(current_value)
            current_length = 1
            current_value = sorted_lst[i]
    lengths.append(current_length)
    values.append(current_value)
    return lengths, values


# Пример использования
lst = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
lengths, values = sort_and_split_list(lst)


print("Длины серий:", lengths)
print("Значения элементов:", values)
