"""
Распечатать все шестизначные числа, в записи
которых нет повторяющихся цифр, и вывести
их количество. Ограничений по использованию циклов и массивов нет.
"""


# Tatiana
def print_unique_six_digit_numbers():
    """Count total amount og numbers that
    consist of unique digits of 6 figures."""
    count = 0
    for num in range(100000, 1000000):
        num_str = str(num)
        if len(set(num_str)) == 6:

            count += 1
    return count


count_unique_numbers = print_unique_six_digit_numbers()
print("Total count of unique six-digit numbers:", count_unique_numbers)

# =======

# def is_pandigital(num):
#     if len(str(num)) != 6:
#         return False
#     return len(set(str(num))) == 6

# count = 0
# for i in range(100000, 1000000):
#     if is_pandigital(i):
#         count += 1

# print(count)

# def is_pandigital (num):
# создание функции и приянтие числа
# if len(str(num)) != 6:
# return False
# return len (set (str (num) )) == 6
# возвращает true если число 6 значное , false если наоборот
# count = 0
# for i in range (100000, 1000000):
# перебор всех 6 ти значных цифр
# if is_pandigital (1):
# count += 1
# счетчик count
# print (count )
# вывод всех чисел удовлетворяющих условие

# аналог через комбинаторику

# from itertools import permutations

# perms = permutations(range(10), 6)

# unique_perms = filter(lambda x: len(set(x)) == 6, perms)

# count = 0
# for perm in unique_perms:
#     num = int(''.join(map(str, perm)))
#     print(num)
#     count += 1

# print(count)
