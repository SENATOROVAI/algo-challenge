def is_pandigital (num):
# создание функции и приянтие числа

if len(str(num)) != 6:
return False
 return len (set (str (num) )) == 6
# возвращает true если число 6 значное , false если наоборот
count = 0
for i in range (100000, 1000000):
# перебор всех 6 ти значных цифр
if is_pandigital (1):
Click to collapse the range.
count += 1
# счетчик count
print (count )
# вывод всех чисел удовлетворяющих условие
