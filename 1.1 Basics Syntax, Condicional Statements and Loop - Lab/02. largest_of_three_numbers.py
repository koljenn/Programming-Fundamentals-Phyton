first_num = int(input())
second_num = int(input())
third_num = int(input())

if first_num > second_num and first_num > third_num:
    print(first_num)
elif second_num >first_num and second_num > third_num:
    print(second_num)
else:
    print(third_num)

# Втори съкратен вариант:

# first_number, second_number, third_number = int(input()), int(input()), int(input())
# print(max(first_number, second_number, third_number))
