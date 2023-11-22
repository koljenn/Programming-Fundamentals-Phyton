# На първия ред ще получите число n. На следващите n реда ще получите цели числа.
# Трябва да създадете и отпечатате два списъка:
# • Едно с всички положителни (включително 0) числа
# • Едно с всички отрицателни числа
# Накрая отпечатайте следното съобщение:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"

number_of_lines = int(input())
positive_numbers = []
negative_numbers = []

for i in range(number_of_lines):
    current_number = int(input())

    if current_number >= 0:
        positive_numbers.append((current_number))
    else:
        negative_numbers.append(current_number)
print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")

