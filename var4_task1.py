"""Дано натуральное число N. Выведите все его цифры
по одной, в обратном порядке, разделяя
их пробелами или новыми строками. При решении
этой задачи нельзя использовать строки,
списки, массивы (ну и циклы, разумеется). 
Разрешена только рекурсия и целочисленная
арифметика."""


 def reverse_digits(number: int)-> int:
     """print digits in reverse order"""

     if number < 10:
         print(number)
     else:
         last_digit: int = number % 10
         print(last_digit, end=" ")
         number //= 10
         return reverse_digits(number)


 input_data = int(input())
 reverse_digits(input_data)
