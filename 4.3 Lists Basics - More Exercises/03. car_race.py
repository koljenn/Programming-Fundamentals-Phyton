# Напишете програма, която обявява победителя в автомобилно състезание.
# Ще получите поредица от числа. Всяко число представлява времето,
# което колата трябва да премине през тази стъпка (индекса). Ще има две коли.
# Първият започва от лявата страна, а другият започва от дясната страна.
# Средният индекс на последователността е финалната линия.
# Изчислете общото време, необходимо на всеки състезател, за да стигне до финалната линия,
# и отпечатайте победителя с общото му време (състезателя с по-малко време).
# Ако имате нула в списъка, трябва да намалите времето на състезателя, който я е достигнал, с 20% (от текущото му време).
# Броят на елементите в последователността винаги ще бъде нечетен.
# Отпечатайте резултата в следния формат "The winner is {left/right} with total time: {total_time}".
# Времето трябва да бъде форматирано до първия десетичен знак.

time_list = input().split()
total_time_left_racer = 0
total_time_right_racer = 0
time_list = [int(time) for time in time_list]
middle = len(time_list) // 2  # The middle index of the sequence is the finish line.
left_racer_time_list = time_list[:middle]
right_racer_time_list = time_list[middle + 1:]
winner = ""
winner_time = 0

if 0 not in left_racer_time_list:
    total_time_left_racer = sum(left_racer_time_list)
else:
    for time in left_racer_time_list:
        if time != 0:
            total_time_left_racer += time
        else:
            total_time_left_racer -= 0.20 * total_time_left_racer

if 0 not in right_racer_time_list:
    total_time_right_racer = sum(right_racer_time_list)
else:
    for index in range(len(right_racer_time_list) - 1, -1, -1):
        if right_racer_time_list[index] != 0:
            total_time_right_racer += right_racer_time_list[index]
        else:
            total_time_right_racer -= 0.20 * total_time_right_racer

if total_time_left_racer > total_time_right_racer:
    winner = "right"
    winner_time = total_time_right_racer
else:
    winner = "left"
    winner_time = total_time_left_racer
print(f"The winner is {winner} with total time: {winner_time:.1f}")