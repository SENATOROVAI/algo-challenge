"""
Для  заданного  четырехзначного  числа  найти  разницу
между  наибольшей  и  наименьшей
цифрой. Ограничений по использованию циклов и массивов нет.
"""

# Кирилл
# global(outer) skope область видимости модуля(файл.py)
# builtins.pyi системная область видимости,видна в любом модуле
# local sсopee переменная объявленная в области функции


def find_difference(num: int) -> int:
    """функция считает разницу между числами"""
    # подсчёт разницы
    # sub_num = int(max(f"{num}")) - int(min(f"{num}"))
    if len(str(num)) != 4:
        raise Exception("Число должно быть четырехзначным")
    for number in str(num):
        max_number: str = str(num)[0]
        min_number: str = str(num)[0]
        if int(max_number) < int(number):
            max_number = number
        # elif int(min_number) > int(number):
        # min_number = number
        else:
            min_number = number

    return int(max_number) - int(min_number)


print(find_difference(num=1234))

# /.Кирилл


# Влад
# number = int(input())
# print(max(list(map(int, str(number)))) - min(list(map(int, str(number)))))
# .\Влад

# senatorov
# sub_num = int(max(f"{num}")) - int(min(f"{num}"))
# .\ Senatorov
