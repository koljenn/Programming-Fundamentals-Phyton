# Вие сте в зоологическата градина и сурикатите изглеждат странно.
# Ще получите 3 стринга на отделни линии, представляващи опашката, тялото и
# главата на животно в този ред. Вашата задача е да пренаредите елементите в списък,
# така че животното отново да изглежда нормално:
# •	On the first position is the head;
# •	On the second position is the body;
# •	On the last one is the tail.

my_list = []

for _ in range(3):  # На _ може да се напише current_list или i
    data = input()
    my_list.append(data)

my_list[0], my_list[2] = my_list[2], my_list[0]  # суапване, разменя местата

print(my_list)


# Втори вариант:
# tail = input()
# body = input()
# head = input()
#
# meerkat = [tail, body, head] # meerkat е сурикат(животно)!
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0] # суапване, разменя местата
# print(meerkat)

# Трети вариант:
# merkat = []
#
# merkat.append(input())
# merkat.append(input())
# merkat.append(input())
#
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
#
# print(meerkat)