string = input().lower()
count = 0

count += string.count("sand")
count += string.count("water")
count += string.count("fish")
count += string.count("sun")

print(count)

# Втори вариант:
#
# word = input().lower()
# words_to_check = "sand", "water", "fish", "sun"
# counter = 0
# counter += word.count("sand")
# counter += word.count("water")
# counter += word.count("fish")
# counter += word.count("sun")
# print(counter)