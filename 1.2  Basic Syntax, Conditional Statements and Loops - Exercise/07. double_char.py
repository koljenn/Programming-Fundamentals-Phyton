# string = input()
# while string != "End":
#     if string != 'SoftUni':
#         for index, char in enumerate(string):
#             if index == len(string):
#                 print(char, end='')
#                 print({char})
#             else:
#                 print(char, end='')
#                 print(char, end='')
#         string = input()
#         print()
#     else:
#         string = input()
#
# Втори вариант:

string = input()
while string != "End":
    if string != 'SoftUni':
        for char in string:
            print(char, end='')
            print(char, end='')
        print()
    string = input()