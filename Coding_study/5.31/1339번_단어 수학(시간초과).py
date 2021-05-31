from itertools import permutations
import copy
n = int(input())

words = []
alpha = []

for i in range(n):
    init_word = list(input().strip())
    # print(init_word,"!!!")
    alpha.append(init_word)
    words.append(init_word)

    # print(words,"words")

words = copy.deepcopy(words)
for i in range(1, len(alpha)):
    alpha[0] += alpha[i]
alpha = set(alpha[0])

# print(alpha)

num = []
for i in range(9,9-len(alpha),-1):
    num.append(i)
# print(alpha)
# print(num)

al = []
for i in alpha:
    al.append(i)

# print(al)

alpha_Case = permutations(al, len(al))
max_value = 0
for case in alpha_Case:
    d = {}
    res = 0
    # a = list(zip(list(i),num))
    nine = 9
    for c in case:
        d[c] = nine
        nine -= 1

    for word in words:
        # print(word)
        idx = len(word) - 1
        for spell in word:
            # print(word, spell,d[spell], idx)
            # print(idx)
            if idx > 0:
                # print("spellll",d[spell] * (10 ** idx))
                res += d[spell] * (10 ** idx)
            else:
                res += d[spell]
            idx -= 1
        # print(res)
    if res > max_value:
        max_value = res
print(max_value)

