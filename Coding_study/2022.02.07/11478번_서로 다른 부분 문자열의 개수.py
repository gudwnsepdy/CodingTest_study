word = str(input())
l = len(word)

dic = dict()

for i in range(l+1):
    for j in range(l+1):
        dic[word[i:j]] = 1

print(len(dic) - 1)