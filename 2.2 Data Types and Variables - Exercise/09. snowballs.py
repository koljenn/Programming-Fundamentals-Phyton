# Тони и Анди обичат да играят в снега и да се бият със снежни топки,
# но винаги спорят кой прави най-добрите снежни топки. Те са решили да ви въвлекат в битката си,
# като напишат програма, която изчислява данни за снежна топка и
# извежда най-добрата стойност на снежна топка.
# Ще получите N – цяло число, броят на снежните топки, направени от Тони и Анди.
# На следващите редове ще получите 3 входа за всяка снежна топка:
# •	The weight of the snowball (integer). Теглото на снежната топка (цяло число).
# •	The time needed for the snowball to get to its target (integer).Времето,
# необходимо на снежната топка да стигне до целта си (цяло число).
# •	The quality of the snowball (integer). Качеството на снежната топка (цяло число).
# За всяка снежна топка трябва да изчислите нейната стойност по следната формула:
# (snowball_weight / snowball_time) ** snowball_quality
# (тегло на снежна топка / време на снежна топка) ** качество на снежна топка
# Input:
# •	On the first input line, you will receive N – the number of snowballs.
# На първия входен ред ще получите N – броя на снежните топки.
# •	On the next N*3 input lines, you will be receiving data about each snowball.
# На следващите N*3 входни реда ще получавате данни за всяка снежна топка.
# Output:
# •	You need to print the highest calculated snowball's value in the format:
# Трябва да отпечатате най-високата изчислена стойност на снежната топка във формата:
# "{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"
# Constraints:Ограничения:
# •	The number of snowballs (N) will be an integer in range [0, 100].
# •	The weight is an integer in the range [0, 1000].
# •	The time is an integer in the range [1, 500].
# •	The quality is an integer in the range [0, 100].

number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0
for current_snowball in range(number_of_snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight / current_time) ** current_quality
    if current_value > max_value:
        max_weight = current_weight
        max_time = current_time
        max_quality = current_quality
        max_value = current_value
print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")
