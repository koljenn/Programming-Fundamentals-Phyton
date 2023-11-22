# На първия ред ще получите едно число n.
# На следващите n реда ще получите имена на курсове.
# Трябва да създадете списък с курсове и да го отпечатате.

number = int(input())
courses_lst = []

for i in range(number):
    course_name = input()
    courses_lst.append(course_name)

print(courses_lst)

# Втори вариант:

# number = int(input())
# courses = list()
#
# for i in range(number):
#     courses.append(input())
#
# print(courses)