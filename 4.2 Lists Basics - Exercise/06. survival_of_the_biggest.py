# Напишете програма, която получава списък от цели числа (разделени с един интервал) и число n.
# Числото n представлява броя на числата за премахване от списъка.
# Трябва да премахнете най-малките и след това да отпечатате всички числа, които са останали в списъка,
# разделени със запетая и интервал ", ".


list_of_integers = input().split()
count_of_numbers_to_remove = int(input())
list_of_integers = [int(integer) for integer in list_of_integers]

for number in range(count_of_numbers_to_remove):
    smallest = min(list_of_integers)
    list_of_integers.remove(smallest)

list_of_integers = [str(string) for string in list_of_integers]

print(', '.join(list_of_integers))