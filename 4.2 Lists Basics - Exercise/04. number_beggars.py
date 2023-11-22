# Ще получите 2 реда за въвеждане. На първия ред ще получите единичен низ от цели числа,
# разделени със запетая и интервал ", ". На втория ред ще получите брой просяци.
# Вашата задача е да отпечатате списък със сбора на това, което всеки просяк носи вкъщи, като приемем,
# че всички се редуват редовно, от първия до последния номер в списъка.
# Например: [1, 2, 3, 4, 5] за 2 просяци ще върне резултат от 9 и 6, като първият взема [1, 3, 5],
# вторият събира [2, 4]. Същият списък с 3-ма просители би дал по-добър резултат за втория просяк: 5, 7 и 3,
# тъй като те съответно ще вземат [1, 4], [2, 5] и [3].
# Също така имайте предвид, че не всички просяци трябва да приемат еднакво количество "оферти", което означава,
# че дължината на списъка не е непременно кратна на n.
# Дължината на списъка може да бъде още по-къса - т.е. последните просяци няма да вземат нищо (0).


money_list = input().split(", ")
# ["1", "2", "3", "4", "5"]
money_list_as_digit = []
for element in money_list:
    money_list_as_digit.append(int(element))
# [1, 2, 3, 4, 5]
number_of_beggars = int(input())
final_sums = []
starting_index = 0
while starting_index < number_of_beggars:
    sum_for_current_beggar = 0
    for current_index in range(starting_index, len(money_list_as_digit), number_of_beggars):
        sum_for_current_beggar += money_list_as_digit[current_index]
    final_sums.append(sum_for_current_beggar)
    starting_index += 1
print(final_sums)
