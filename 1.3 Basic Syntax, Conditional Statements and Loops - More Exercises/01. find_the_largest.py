# Ще ви бъде даден номер. Отпечатайте най-голямото число, което може да се образува от цифрите на даденото число.

number = int(input())
list_digits = []

for digit in (str(number)):
    list_digits.append(digit)
    list_digits.sort(reverse=True)
print(''.join(list_digits))

# Втори вариант:
#
# number = input()
# largest_digit = []
# for digit in number:
#     digit = int(digit)
#     largest_digit.append(digit)
# largest_digit.sort()
# print(*largest_digit[::-1], sep="")