n = int(input())

word = str(input())
idx = word.index("*")

first_word = word[:idx]
# print(word[-(len(word) - idx) + 1:])
last_word = word[-(len(word) - idx) + 1:]

# print(first_word, last_word)

dir_list = []
for _ in range(n):
    dir_name = str(input())
    dir_list.append(dir_name)

for dir_name in dir_list:

    if len(dir_name) < len(first_word + last_word):
        print("NE")
        continue

    if first_word == dir_name[:idx] and last_word == dir_name[-(len(word) - idx) + 1:]:
        print("DA")
    else:
        print("NE")
