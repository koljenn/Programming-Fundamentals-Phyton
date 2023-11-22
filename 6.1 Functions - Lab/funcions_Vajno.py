# 1. lambda funcions: Анонимни функции

# x = lambda a: a + 10 # Взимаме аргумент и добавяме 10
# print(x(5)) # аргумент
# Връща 15
# С функция се прави така, същото е:
# def plus_five(a):
#     return a + 5
# print(plus_five(10))
# Пак връща 15

# 2.
# x = lambda a, b: a * b
# print(x(3, 4))
# Връща 12

# 3.
# full_name = lambda first, last: f"I am {first} {last}"
# result = full_name("Guido", "van Rossum")
# print(result)
# Връща: I am Guido van Rossum

# 4. Умножение на стринг и каунт(брояч или цифра):
# Вариант А:
# def repeater(str, count):
#     for i in range(count):
#         new_str += str
#     return new_str
#
# Вариант Б, съкратен на горния:
# def repeater(str, count):
#     return str * count
#
# Вариант с ламбда:
# repeater = lambda str, count: str * count

# 5.
# print("*" * n) където n е 3(примерно) отпечатва ***


