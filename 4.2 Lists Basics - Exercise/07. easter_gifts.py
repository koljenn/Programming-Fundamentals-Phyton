# Като добър приятел решавате да купите подаръци за приятелите си.
# Създайте програма, която ви помага да планирате подаръците за вашите приятели и семейство.
# Първо, вие ще получите подаръците, които планирате да купите, на един ред, разделени с интервал,
# в следния формат: „{gift1} {gift2} {gift3}… {giftn}“
# След това ще започнете да получавате команди, докато не прочетете съобщението „Няма пари“.
# Има три възможни команди:
# • „Изчерпан {подарък}“
# o Намерете подаръците с това име във вашата колекция, ако има такива, и променете техните стойности на „None“.
# • „Задължително {gift} {index}“
# o Ако индексът е валиден, заменете подаръка в дадения индекс с дадения подарък.
# • „JustInCase {подарък}“
# o Заменете стойността на последния си подарък с този.
# Накрая отпечатайте подаръците на един ред, с изключение на тези със стойност "Няма",
# разделени с един интервал в следния формат: „{gift1} {gift2} {gift3} … {giftn}“
# Вход / Ограничения
# • На 1-ви ред ще получите имената на подаръците, разделени с един интервал.
# • На следващите редове, докато не бъде получена командата "Няма пари", вие ще получавате команди.
# • Въведеното винаги ще бъде валидно.
# Изход
# • Отпечатайте подаръците в описания по-горе формат.


gifts = input().split()

command = input()
while command != "No Money":
    command = command.split()
    if command[0] == "OutOfStock":  # "OutOfStock {gift}"
        # Find the gifts with this name in your collection, if any, and change their values to "None".
        for index in range(len(gifts)):
            if command[1] == gifts[index]:
                gifts[index] = "None"
    elif command[0] == "Required":  # "Required {gift} {index}"
        # If the index is valid, replace the gift on the given index with the given gift.
        index = int(command[2])
        if 0 < index < len(gifts):
            gifts[index] = command[1]
    elif command[0] == "JustInCase":  # "JustInCase {gift}"
        # Replace the value of your last gift with this one.
        gifts[-1] = command[1]
    command = input()

# Print the gifts on a single line, except the ones with value "None", separated by a single space.
if "None" in gifts:
    for element in range(len(gifts) - 1, -1, -1):
        if "None" in gifts[element]:
            gifts.remove(gifts[element])

print(' '.join(gifts))