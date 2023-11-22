# Напишете програма, която получава единичен низ,
# съдържащ положителни и отрицателни числа,
# разделени с един интервал. Отпечатайте списък, съдържащ обратното на всяко число.

list_of_numbers = input().split()
opposite_numbers = []
for element in list_of_numbers:
    current_number = -int(element)
    opposite_numbers.append(current_number)
print(opposite_numbers)