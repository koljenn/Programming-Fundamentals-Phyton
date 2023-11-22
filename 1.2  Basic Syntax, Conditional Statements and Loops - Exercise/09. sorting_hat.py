# name = input()
# while name != "Voldemort":
#     name = input()
#     if name == "Welcome!":
#         print(f"Welcome to Hogwarts.")
#     if name == "Voldemort":
#         print("You must not speak of that name!")
#         break
#     character_counter = len(name)
#     if character_counter < 5:
#         print(f"{name} goes to Gryffindor.")
#     elif character_counter == 5:
#         print(f"{name} goes to Slytherin.")
#     elif character_counter == 6:
#         print(f"{name} goes to Ravenclaw.")
#     elif character_counter > 6:
#         print(f"{name} goes to Hufflepuff.") не е верен този вариант

command = input()

welcome = True

while command != "Welcome!":

    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6 and command != "Voldemort":
        print(f"{command} goes to Hufflepuff.")
    elif command == "Voldemort":
        print("You must not speak of that name!")
        welcome = False
        break

    command = input()

if welcome:
    print("Welcome to Hogwarts.")
