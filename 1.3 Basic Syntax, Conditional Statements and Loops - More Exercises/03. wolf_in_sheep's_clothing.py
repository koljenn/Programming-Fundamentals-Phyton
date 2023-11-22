# string_animals = input()
# list_animals = string_animals.split(", ")
#
# for number in range(len(list_animals), 0, -1):
#     # print(number, end=" ")
#     # print(list_animals[-number])
#     if list_animals[-1] == "wolf":
#         print("Please go away and stop eating my sheep")
#         break
#     elif list_animals[-number] == "wolf":
#         print(f"Oi! Sheep number {number - 1}! You are about to be eaten by a wolf!")
#
# Втори вариант:

text = input()

check_for_wolf = text.split(", ")
check_for_number = len(check_for_wolf) - 1

for wolf in check_for_wolf:

    if wolf == "wolf" and check_for_number == 0:
        text_to_print = "Please go away and stop eating my sheep"

    elif wolf == "wolf":
        text_to_print = f"Oi! Sheep number {check_for_number}! You are about to be eaten by a wolf!"

    check_for_number -= 1

print(text_to_print)