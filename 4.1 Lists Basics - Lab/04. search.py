# На първия ред ще получите число n. На втория ред ще получите дума.
# На следващите n реда ще ви бъдат дадени низове.
# Трябва да ги добавите към списък и да ги отпечатате.
# След това трябва да филтрирате само низовете, които включват дадената дума,
# и да отпечатате и този списък.

number = int(input())
key = input()
list_all = []
filtered_list = []

for word in range(number):
    string = input()
    list_all.append(string)
    if key in string:
        filtered_list.append(string)

print(list_all)
print(filtered_list)

# Втори вариант:
# number = int(input())
# search_word = input()
# strings = list()
#
# for i in range(number):
#     strings.append(input())
# print(strings)
#
# filtered = list()
# for current_string in strings:
#     filtered.append(current_string)
# print(filtered)
