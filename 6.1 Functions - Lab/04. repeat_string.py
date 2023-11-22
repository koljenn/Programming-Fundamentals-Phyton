# Напишете функция, която получава низ и брояч n.
# Функцията трябва да върне нов низ(string) – резултатът от повторението на стария низ n пъти.
# Отпечатайте резултата от функцията. Опитайте да използвате ламбда.

string = input()
number = int(input())
result = lambda string, num: string * num
print(result(string, number))

# Втори вариант на Ангел Георгиев:

# repeater = lambda str, count: str * count
#
# current_string = input()
# current_count = int(input())
#
# print(repeater(current_string, current_count))