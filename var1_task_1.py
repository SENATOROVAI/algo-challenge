"""
Дано натуральное число N. Выведите все его цифры по одной,
в обратном порядке, разделяя
их пробелами или новыми строками. При решении этой задачи
нельзя использовать строки,
списки, массивы (ну и циклы, разумеется). Разрешена только
рекурсия и целочисленная арифметика.
"""


# Влад
def reverse_digits(number):
    """print digits in reverse order"""

    if number < 10:
        print(number)
    else:
        last_digit = number % 10
        print(last_digit, end=" ")
        number //= 10
        reverse_digits(number)


input_data = int(input())
reverse_digits(input_data)
# .\Влад

# SENATOROV
# def print_digits(n):
#   """Prints the digits of a natural number N in reverse order,
# separated by spaces.

#   Args:
#     n: A natural number (non-negative integer).

#   Raises:
#     ValueError: If n is negative.
#   """

#   if n < 0:
#     raise ValueError("Input n must be a non-negative integer.")

#   if n == 0:
#     return

#   print_digits(n // 10)
#   print(n % 10, end=" ")

#
# print_digits(12345)  # Output: 5 4 3 2 1
# .\SENATOROV
