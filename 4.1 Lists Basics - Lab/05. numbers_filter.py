# На първия ред ще получите едно число n. На следващите n реда ще получите цели числа.
# След това ще ви бъде дадена една от следните команди:
# •	even
# •	odd
# •	negative
# •	positive
# Филтрирайте всички числа, които се вписват в категорията (0 се счита за положително и четно).
# Накрая отпечатайте резултата.

number_of_lines = int(input())
# constant values
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_POSITIVE = 'positive'
COMMAND_NEGATIVE = 'negative'
# accepting numbers from user input
numbers = []

for _ in range(number_of_lines):
    current_number = int(input())
    numbers.append(current_number)

command = input()

filtered_numbers = []
# number_filtering
for number in numbers:
    filtered_passes = (
            (command == COMMAND_EVEN and number % 2 == 0) or
            (command == COMMAND_ODD and number % 2 != 0) or
            (command == COMMAND_NEGATIVE and number < 0) or
            (command == COMMAND_POSITIVE and number >= 0)
    )
    if filtered_passes:
        filtered_numbers.append(number)

print(filtered_numbers)

# Втори вариант на Митко Втори:
#
# lines = int(input())
# command_even = "even"
# command_odd = "odd"
# command_positive = "positive"
# command_negative = "negative"
# my_list = []
# filtered_numbers = []
#
# for num in range(lines):
#     curr_num = int(input())
#     my_list.append(curr_num)
#
# command = input()
#
# for number in my_list:
#     filtered_command = (
#         (command == command_even and number % 2 == 0) or
#         (command == command_odd and number % 2 != 0) or
#         (command == command_positive and number >= 0) or
#         (command == command_negative and number < 0)
#     )
#
#     if filtered_command:
#         filtered_numbers.append(number)
#
# print(filtered_numbers)

# Трети вариант по разтеглен от лектор:
# number = int(input())
#
# positive = list()
# negative = list()
# odd = list()
# even = list()
#
# for i in range(number):
#     current = int(input())
#     if current % 2 == 0:
#         even.append(current)
#     else:
#         odd.append(current)
#     if current >= 0:
#         positive.append(current)
#     else:
#         negative.append(current)
#
# filter_word = input()
#
# if filter_word == "even":
#     print(even)
# if filter_word == "odd":
#     print(odd)
# if filter_word == "positive":
#     print(positive)
# if filter_word == "negative":
#     print(negative)

# Четвърти вариант с eval:
# number = int(input())
#
# positive = list()
# negative = list()
# odd = list()
# even = list()
#
# for i in range(number):
#     current = int(input())
#     if current % 2 == 0:
#         even.append(current)
#     else:
#         odd.append(current)
#     if current >= 0:
#         positive.append(current)
#     else:
#         negative.append(current)
#
# filter_word = input()
#
# print(eval(filter_word)) # Отпечатай списъка, който съм създал!!! Казва се рефлекшън!
