# 1.
# examle_lst = ["ivan", "pesho", "ivan", "ivan", "ivan"]
# Може да съдържа всякакви стойности! С ПРАВОЪГЪЛНИ СКОБИ ЗА ЛИСТОВЕТЕ!
# Може и да се повтарят!

# 2.
# examle_lst = ["ivan", 4, int, str, 4.55]
# Може всичко да съдържа! В практиката обаче се съхраняват повече ЕДНОТИПНИ данни! Примерно:
# username = ["ivan", "pesho", "gosho"]
# numbers = [1, 2, 3, 5.5]

# 3. Празен списък:
# empty_list = list() или
# my_list = []

# 4. split Сплитване: РАЗДЕЛЯНЕ
# some_text = "a b c d"
# my_list = some_text.split(" ") # сепаратор(може да е всичко - интервал, знак ...)
# print(my_list)
# Резултат: ['a', 'b', 'c', 'd']

# 5. join Джойнване: ОБЕДИНЯВАНЕ
# my_list = ["a", "b", "c"] # ВАЖНО: Само стрингове, с числа не става!!!
# print("-".join(my_list))
# Резултат: a-b-c

# 6. index Индексиране: ДОСТЪПВАНЕ ПО ИНДЕКС
# list_of_numbers = [1, 5, 7]
# print(list_of_numbers[0]) # 1
# print(list_of_numbers[1]) # 5
# print(list_of_numbers[2]) # 7
# Индексацията почва от 0 както винаги!Може и на обратно с -1 от последния символ в списъка!

# 7. append Добаване на елемент в списъка:
# emppty_list = []
# emppty_list.append(2)
# emppty_list.append(3)
# print(emppty_list)
# Резултат: [2, 3]

# 8. remove Премахване на конкретен елемент, не индекс!!! Число, стринг и т.н.
# list_of_numbers = [1, 2, 3, 4, 5]
# list_of_numbers.remove(3)
# list_of_numbers.remove(1)
# print(list_of_numbers)
# Резултат: [2, 4, 5] # Ако напишем remove[3], ще премахне 4-ката, защото е по индекс 4!

# 9. len:
# my_list =["dog", "cat", "fish"]
# for element in my_list:
#     print(element, end=" ")
# Резултат: dog cat fish  # С разстояние, защото сме го задали в end="_" с разстояние между кавичките!
# Важно:
# my_list =["dog", "cat", "fish"]
# for index in range(len(my_list)):  # len връща колко елемента има в списъка като бройка! По индекс 0,1,2!
#     print(my_list[index], end=" ")
# Резултата пак е: dog cat fish
# ВАЖНО: ДВЕТЕ НЕЩА РАБОТЯТ ПО ЕДИН И СЪЩИ НАЧИН!
# КОГАТО ИСКАМЕ ДА РАЗГЛЕЖДАМЕ ЕЛЕМЕНТИТЕ ОТ СПИСЪКА, ПОЛЗВАМЕ ГОРНИЯ НАЧИН!
# ДОЛНИЯ НАЧИН МОЖЕ ДА СЕ СРЕЩНЕ ЧЕСТО, КОГАТО ИСКАМЕ ДА ИМАМ ИНДЕКС И ДА ИТЕРИРАМЕ ПРЕЗ НЯКОЛКО СТРУКТУРИ
# ДАННИ ЕДНОВРЕМЕННО! АКО ИМАМЕ ДВА СПИСЪКА, МОЖЕМ ДА ВЗИМАМЕ ПЪРВИЯ ЕЛЕМЕНТ ОТ ДВАТА СПИСЪКА,
# ВТОРИЯ ЕЛЕМЕНТ ОТ ДВАТА СПИСЪКА, ТРЕТИЯ ЕЛЕМЕНТ ОТ ДВАТА СПИСЪКА!
# ТОГАВА Е НАЙ-ДОБРЕ ДА НАПРАВИМ index И ДА ВЗИМАМЕ my_list1 index, my_list2 index И ТОГАВА СЪС
# ЕДИН И СЪЩИ ИНДЕКС МОЖЕМ ДА ОБХОЖДАМЕ ПОВЕЧЕ ОТ ЕДИН СПИСЪК!

# 10.while # До като списъка не е пълен!
# my_list = ["dog", "cat", "fish"]
# i = 0
# while i < len(my_list):
#     print(my_list[i], end=" ")
#     i += 1
# Резултат: dog cat fish # Това е for цикъл, разбит на while! Имаме нула, събираме с 1 до като стигне дължината!
# Втори вариант:
# my_list = ["dog", "cat", "fish"]
# while my_list:
#     print(my_list[0], end=" ")
#     current_element = my_list[0]  # Временна променлива, и изтриваме елемента, който е на временната променлива!
#     my_list.remove(current_element)
# Ще взима всеки първи елемент, до като съществува списъка! До като този списък има елементи, това ще бъде true!
# Когато свършат елементите, ще стане false и ще спре да се изпълнява!

# 11. in  Проверка, дали елемент е в списъка:
# my_list = [1, 2, 3, 4]
# if 3 in my_list:  # in е логически израз!
#     print(f"The number 3 is in the list")

# 12. not in  Проверка, дали елемент не е в списъка:
# my_list = [1, 2, 3, 4]
# if 5 not in my_list:
#     print(f"The number 5 is not in the list")

# 13. eval Виж задача 5 за тази команда!!! Казва се рефлекшън!


14.

