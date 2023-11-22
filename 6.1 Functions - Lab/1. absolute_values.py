# Write a program that receives a sequence of numbers, separated by a single space,
# and prints their absolute value as a list. Use abs().

numbers = input().split(' ')
abs_numbers = []

for num in numbers:
    abs_numbers.append(abs(float(num)))

print(abs_numbers)

# numbers = list(map(float, input().split(' ')))
# result = [abs(num) for num in numbers]
# print(result)