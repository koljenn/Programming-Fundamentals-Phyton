# Фаро разбъркването е метод за разбъркване на тесте карти,
# при което тестето се разделя точно наполовина. След това картите в двете половини са идеално преплетени,
# така че оригиналната долна карта все още е отдолу, а оригиналната горна карта е все още отгоре.
# Например, faro разбърква
# списъка ['ace', 'two', 'three', 'four', 'five', 'six'] веднъж, дава ['ace', 'four', 'two', 'five ', 'three', 'six']
# Напишете програма, която получава единичен низ (карти, разделени с интервал)
# и на втория ред получава броене на фаро разбърквания, които трябва да бъдат направени.
# Отпечатайте състоянието на тестето след разбъркването.
# Забележка: Дължината на тестето карти винаги ще бъде четно число.


deck_of_cards = input().split()
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0: middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck::]
    for card_index in range(len(left_part)):
        final_deck.append(left_part[card_index])
        final_deck.append(right_part[card_index])
    deck_of_cards = final_deck
print(deck_of_cards)
