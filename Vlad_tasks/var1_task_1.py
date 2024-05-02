"""task of algo_test"""


def reverse_digits(number):
    """print in reverse order"""

    if number < 10:
        print(number)
    else:
        last_digit = number % 10
        print(last_digit, end=" ")
        number //= 10
        reverse_digits(number)


input_data = int(input())
reverse_digits(input_data)
