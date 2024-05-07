"""
Напишите программу, которая сортирует список, а затем
находит максимальное из тех чисел, что встречаются в
 массиве три раза и более. Не использовать встроенные функции.
"""

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
