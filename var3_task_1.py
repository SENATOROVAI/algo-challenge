"""Дано натуральное число N. Вычислите сумму его цифр. При решении этой задачи нельзя
использовать строки, списки, массивы (ну и циклы, разумеется)."""


def sum_of_digits(num_1):
    if num_1 == 0:
        return 0
    return num_1 % 10 + sum_of_digits(num_1 // 10)


num = int(input("Введите натуральное число: "))
total_sum = sum_of_digits(num)
print("Сумма цифр числа", num, "равна", total_sum)
