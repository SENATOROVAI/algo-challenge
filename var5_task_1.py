"""Write var5_task1."""


"""Дано натуральное число N 
Выведите все его цифры по одной 
обычном порядке, разделяя
их пробелами или новыми строками.При решении этой задачи нельзя
использовать строки,
списки, массивы (ну и циклы, разумеется). 
Разрешена только рекурсия и целочисленная
арифметика."""


def print_digits(num):
    if num < 10:
        print(num)
    else:
        print_digits(num // 10)
        print(num % 10)


# Пример использования
num = 123456
print_digits(num)