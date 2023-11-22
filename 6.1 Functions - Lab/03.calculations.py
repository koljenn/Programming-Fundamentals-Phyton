
# Създайте функция, която получава три параметъра, изчислява резултат в зависимост от дадения оператор и го връща.
# Отпечатайте резултата от функцията.
# Входът идва като три параметъра – оператор като низ и две цели числа.
# Операторът може да бъде един от следните: "умножение", "деление", "събиране", "изваждане".

def calculation_func(number_a, number_b, operation):
    if operation == "multiply":
        return number_a * number_b

    elif operation == "divide":
        return int(number_a / number_b) # Има int, защото делението трябва да върне цяло число, не float

    elif operation == "add":
        return number_a + number_b

    elif operation == "subtract":
        return number_a - number_b


type_of_operation = input()
first_number = int(input())
second_number = int(input())
print(calculation_func(first_number, second_number, type_of_operation))