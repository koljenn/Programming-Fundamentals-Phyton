# Създайте функция, която изчислява и връща площта на правоъгълник по зададени ширина и височина.
# Отпечатайте резултата на конзолата.

area_rectangle = lambda width, height: width * height

input_width = int(input())
input_height = int(input())

result = area_rectangle(input_width, input_height)
print(result)

# Втори вариант:

# def area_calc(width,heigth):
#     return width * heigth
#
# current_w = int(input())
# current_h = int(input())
#
# print(area_calc(current_w, current_h))
