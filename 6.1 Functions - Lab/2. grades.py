# Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words.
# •	2.00 – 2.99 - "Fail"
# •	3.00 – 3.49 - "Poor"
# •	3.50 – 4.49 - "Good"
# •	4.50 – 5.49 - "Very Good"
# •	5.50 – 6.00 - "Excellent"

# 1. Първи вариант(Марио Захариев):
# def type_of_grade(score):
#     if 2.00 <= score <= 2.99:
#         return 'Fail'
#     elif 3.00 <= score <= 3.49:
#         return "Poor"
#     elif 3.50 <= score <= 4.49:
#         return "Good"
#     elif 4.50 <= score <= 5.49:
#         return "Very Good"
#     elif 5.50 <= score <= 6.00:
#         return "Excellent"
#
#
# score = float(input())
# print(type_of_grade(score))

# 2. Втори вариант(Ангел Георгиев):
def grade_text():
    if grade_number < 3:
        return "Fail"
    elif grade_number < 3.5:
        return "Poor"
    elif grade_number < 4.5:
        return "Good"
    elif grade_number < 5.5:
        return "Very Good"
    else:
        return "Excellent"
grade_number = float(input())

print(grade_text())

# 3. Трети вариант:
#
# def grade_function(grade):
#     if grade < 3:
#         return "Fail"
#     elif grade < 3.50:
#         return "Poor"
#     elif grade < 4.50:
#         return "Good"
#     elif grade < 5.50:
#         return "Very Good"
#     else:
#         return "Excellent"
#
#
# print(grade_function(float(input())))