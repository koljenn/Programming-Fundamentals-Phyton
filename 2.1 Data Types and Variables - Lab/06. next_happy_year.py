year = int(input())
happy_year_condition = False

while not happy_year_condition:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])  # add добавя към set_year по индекси на годината

    happy_year_condition = len(set_year) == len(str(year)) # Тука проверява True или False

print(year)

# Втори вариант с тюпъл:
# from itertools import permutations
#
# number = tuple(map(int, input()))
# myperm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(number))
#
# for digits in list(myperm):
#     if digits > number:
#         result = ''.join(str(x) for x in digits)
#         print(result)
#         break