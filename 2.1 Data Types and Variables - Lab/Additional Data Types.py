
# 1. list: ,поредица, в която се съхраняват някакви стойности!
# cars = ["Saab", "Volvo", "BMW"]

# 2. Поредица от вложени във вложени списъци:
# example_list = [[1, 2, [4, 4]], [3, 4], [5, 6]]
# print(example_list[-1])
# Пробвай различни варианти и виж какво връща!!! Нарича се МАТРИЦИ! Ползва се за пикселизация!

# 3.
# example_list = [i for i in range(1,11) if i % 2 == 0]
# print(example_list)
# Ще върне [2, 4, 6, 8, 10]. Ако няма if i % 2 == 0, ще печати от 1 до 10!

# 4. tuple: Тюпъл!
# example_tuple = ("apple", "banana", "cherry")
# print(example_tuple)
# Ще върне ('apple', 'banana', 'cherry')! Тюпълите са мютабъл - не се променят!!!

# 5. Разлики:
# example_tuple = ("a", "b", "c")
# example_list = ["a", "b", "c"]
# example_set = {"a", "b", "c"}
#
# print(example_tuple)
# print(example_list)
# print(example_set)
# Само сет променя позициите и премахва дублираните символи!!!

# 6. Сортиране на листове:
# example_list = sorted(["c", "a", "b"])
# print(example_list)
# Сортира по азбучен ред!!! ['a', 'b', 'c']

# example_list = sorted([9, 5, 2, 1, 3, 0])
# print(example_list)
# Връща [0, 1, 2, 3, 5, 9]

# 7. None:
# if null_variable is None:
#     print("null_variable is None")
# # или
# if null_variable == None:
#     print("null_variable is None")
# Дефинираме None като променлива, когато все още не знаем резултата!!!
# Ако не знаем какво очакваме, ползваме None! А не 0!