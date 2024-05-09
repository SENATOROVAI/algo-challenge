"""Write task 5."""
"""Для заданного четырехзначного числа найти
разницу между наибольшей и наименьшей
цифрой. Ограничений по использованию
циклов и массивов нет."""



def find_difference(n : int) -> int:
    n_new = str(n)
    ls = list(n_new)
    return int(max(ls)) - int(min(ls))


print(find_difference(4567))
