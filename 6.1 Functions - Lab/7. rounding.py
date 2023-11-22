# Напишете програма, която закръгля всички дадени числа, разделени с един интервал,
# и отпечатва резултата като списък.
# Използвайте round().

# 1. Първи вариант: не работи???
#
result = list(map(lambda x: round(float(x)), input().split(' ')))

print(result)

# 2. Втори вариант:

# def round_function(list_floats: list):
#     result_list = [round(element) for element in list_floats]
#     # for element in list_floats:
#     #     number = round(element)
#     #     result_list.append(number)
#     return result_list


input_list = input().split()
input_list = [float(i) for i in input_list]

print(round_function(input_list))