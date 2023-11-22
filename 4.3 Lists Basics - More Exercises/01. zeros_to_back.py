# Напишете програма, която получава единичен низ (цели числа, разделени със запетая и интервал ", "),
# намира всички нули и ги премества назад, без да обърква другите елементи.
# Отпечатайте получения списък с цели числа.

list_numbers = input().split(", ")
list_numbers = [int(integer) for integer in list_numbers]
for number in list_numbers:
    if number == 0:
        list_numbers.remove(0)
        list_numbers.append(0)
print(list_numbers)