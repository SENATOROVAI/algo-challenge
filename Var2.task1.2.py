def print_digits (N):
# создание функции
if N < 10:
# создание условия N<10
print (N)
else:
print_digits
N // 10,
# создание условия целочисленное деление (последняя цифра )
print (N % 10)
# остаок от деление
print_digits (12345)
