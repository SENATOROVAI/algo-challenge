"""Find digits in number"""

number = int(input())
print(max(list(map(int, str(number)))) - min(list(map(int, str(number)))))
