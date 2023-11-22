# Напишете функция, която изчислява общата цена на поръчка и я връща.
# Функцията трябва да получи един от следните продукти: "кафе", "кола", "вода" или "закуски" и количество от продукта.
# Цените за единична бройка от всеки продукт са:
# • кафе - 1,50лв
# • вода - 1.00
# • кокс - 1.40

# Първи вариант:

def calc_price(product, quantity):
    if product == "coffee":
        return quantity * 1.5
    elif product == "coke":
        return quantity * 1.4
    elif product == "water":
        return quantity * 1
    elif product == "snacks":
        return quantity * 2

current_product = input()
current_quantity = int(input())

final_price = calc_price(current_product, current_quantity)

print(f"{final_price:.2f}")

# Втори вариант:

# total_price = lambda product_price, quantity: product_price * quantity
#
# input_product = input()
# input_quantity = int(input())
#
# price = 0
# if input_product == "coffee":
#     price = 1.50
# elif input_product == "water":
#     price = 1.00
# elif input_product == "coke":
#     price = 1.40
# elif input_product == "snacks":
#     price = 2.00
#
# total_sum = total_price(price, input_quantity)
# print(f"{total_sum:.2f}")
