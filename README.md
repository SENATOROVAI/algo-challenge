# После скачивания репы, в терминале выполнить:
### pip install pre-commit
### pre-commit install
### pre-commit run --all-files

# Суть челленджа (Рефакторинг):
Постараться улучшить код другого участника, написать эталонный алгоритм. Показать асимптотику. Код другого учатника комментируем, пишем свой над ним, например:

При написании кода обязательно подписывайте свой код:
### \#\#\# Влад
code here:
### \#\#\# .\Влад


# Внимание название файлов такое же как в зачет.пдф, только в начале файла пишем номер варианта, например:
# var1_task_1.1.py

# example изначальный код:
var1_task_1.1.py

"""
Дано натуральное число N. Выведите все его цифры по одной, в обратном порядке, разделяя  
их пробелами или новыми строками. При решении этой задачи нельзя использовать строки,  
списки, массивы (ну и циклы, разумеется). Разрешена только рекурсия и целочисленная  
арифметика.
"""

Влад скопировал мой код, закомментил, и улучшил.

### Влад
def print_digits(n):
    """Prints the digits of a natural number N in reverse order, separated by spaces.

    Args:
        n: A natural number (non-negative integer).

    Raises:
        ValueError: If n is negative.
    """

    if n < 0:
        raise ValueError("Input n must be a non-negative integer.")

    while n:
        # Extract the last digit using bitwise AND operation
        last_digit = n & 1
        print(last_digit, end=" ")

        # Remove the last digit using bitwise right shift
        n >>= 1

# Example usage:
print_digits(12345)  # Output: 5 4 3 2 1
### .\Влад

### SENATOROV 
def print_digits(n):
  """Prints the digits of a natural number N in reverse order, separated by spaces.

  Args:
    n: A natural number (non-negative integer).

  Raises:
    ValueError: If n is negative.
  """

  if n < 0:
    raise ValueError("Input n must be a non-negative integer.")

  if n == 0:
    return

  print_digits(n // 10)
  print(n % 10, end=" ")

# Example usage:
print_digits(12345)  # Output: 5 4 3 2 1
### .\SENATOROV
