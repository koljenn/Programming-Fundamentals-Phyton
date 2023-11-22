# Като гладиатор, Питър трябва да поправи счупеното си оборудване, когато загуби битка.
# Екипировката му се състои от шлем, меч, щит и броня.
# Ще получите броя на загубените битки на Питър.
# Всяка втора загубена игра шлемът му е счупен.
# Всяка трета загубена игра мечът му е счупен.
# Когато мечът и шлемът му са счупени в една и съща загубена битка, щитът му също се счупва.
# Всеки втори път, когато щитът му се счупи, бронята му също трябва да бъде поправена.
# Ще получите цената на всеки артикул в оборудването му.
# Изчислете разходите му за годината за обновяване на оборудването му.
# The input will consist of 5 lines:
# •	On the first line, you will receive the lost fights count – an integer in the range [0, 1000].
# На първия ред ще получите броя на загубените битки – цяло число в диапазона [0, 1000].
# •	On the second line, you will receive the helmet price - a floating-point number in the range [0, 1000].
# На втория ред ще получите цената на каската - число с плаваща запетая в диапазона [0, 1000].
# •	On the third line, you will receive the sword price - a floating-point number in the range [0, 1000].
# На третия ред ще получите цената на меча - число с плаваща запетая в диапазона [0, 1000].
# •	On the fourth line, you will receive the shield price - a floating-point number in the range [0, 1000].
# На четвъртия ред ще получите цената на щита - число с плаваща запетая в диапазона [0, 1000].
# •	On the fifth line, you will receive the armor price - a floating-point number in the range [0, 1000].
# На петия ред ще получите цената на бронята - число с плаваща запетая в диапазона [0, 1000].
#
# As output, you must print Peter`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"
# Като резултат трябва да отпечатате общите разходи на Петър за ново оборудване: "Разходи на гладиатор: {разходи} ауреус"

number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmets_broken = number_of_lost_fights // 2
total_swords_broken = number_of_lost_fights // 3
total_shields_broken = number_of_lost_fights // 6 #number_of_lost_fights // (2*3)
total_armors_broken = total_shields_broken // 2
expenses = helmet_price * total_helmets_broken + \
    sword_price * total_swords_broken + \
    shield_price * total_shields_broken + \
    armor_price * total_armors_broken
print(f"Gladiator expenses: {expenses:.2f} aureus")


