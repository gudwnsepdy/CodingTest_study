from collections import defaultdict

n = int(input())
word_list = []
for i in range(n):
    word_list.append(str(input()))

alpha_dict = defaultdict(int)

for word in word_list:
    for i in range(len(word)):
        alpha_dict[word[i]] += 10 ** (len(word) - 1 - i)

num_list = sorted(list(alpha_dict.values()), reverse=True)

cnt = 9
res = 0

for i in num_list:
    res += cnt * i
    cnt -= 1

print(res)