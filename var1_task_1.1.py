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

print_digits(12345)  
### .\Влад

### SENATOROV 
# def print_digits(n):
#   """Prints the digits of a natural number N in reverse order, separated by spaces.

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
### .\SENATOROV
