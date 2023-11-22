n = int(input())
for num in range(1, n + 1):
    sum_of_digits = 0
    digits = num
    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits /10)
    if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')

# Втори вариант с булева променлива:
# number = int(input())
# for digit in range(1, number + 1):
#     working_number = digit
#     special_number = 0
#     is_special = False
#     while working_number > 0:
#         special_number += working_number % 10
#         working_number = working_number // 10
#     if special_number == 5 or special_number == 7 or special_number == 11:
#         is_special = True
#     print(f"{digit} -> {is_special}")