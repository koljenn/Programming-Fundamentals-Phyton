# Напишете програма, която взема един низ и отпечатва списък с всички индекси с главни букви.

string = input()
list_index = []

for i in range(len(string)):
    if string[i].isupper():
        list_index.append(i)

print(list_index)

# Втори вариант:
#
# string = input()
# index_list = []
#
# for index, letter in enumerate(string):
#     if letter.isupper():
#         index_list.append(index)
#
# print(index_list)