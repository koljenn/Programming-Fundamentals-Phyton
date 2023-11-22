# Като млад авантюрист, вие пътувате с групата си по целия свят, търсейки злато и слава.
# Но трябва да разделите печалбата между своите спътници.
# Ще получите размер на групата. След това получавате дните на приключението.
# Всеки ден печелите 50 монети, но също така харчите по 2 монети на спътник за храна.
# На всеки 3-ти (трети) ден организирате мотивационно парти,
# като харчите по 3 монети на спътник за питейна вода.
# На всеки 5-ти (пети) ден убивате чудовище-бос и печелите 20 монети на спътник.
# Но ако имате мотивационно парти в същия ден, харчите допълнителни 2 монети на спътник.
# На всеки 10 (десети) ден в началото на деня 2 (двама) от вашите спътници напускат,
# но на всеки 15 (петнадесети) ден 5 (пет) нови спътника се присъединяват в началото на деня.
# Трябва да изчислите колко монети получава всеки спътник в края на приключението.
# Входът ще се състои точно от 2 реда:
# •	group size – integer in the range [1…100]
# •	days – integer in the range [1…100]
# Output:
# Print the following message: "{companions_count} companions received {coins} coins each."
# Забележка: Не можете да разделите монета, така че трябва да закръглите монетите до цяло число.

companions = int(input())
days = int(input())
coins = 0
for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        companions -= 2
    if current_day % 15 == 0:
        companions += 5
    if current_day % 3 == 0:
        coins -= 3 * companions
    if current_day % 5 == 0:
        coins += 20 * companions
        if current_day % 3 == 0:
            coins -= 2 * companions
    coins += 50
    coins -= 2 * companions
coins_per_companion = int(coins // companions)
print(f"{companions} companions received {coins_per_companion} coins each.")
