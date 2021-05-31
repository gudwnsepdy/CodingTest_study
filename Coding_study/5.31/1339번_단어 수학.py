n = int(input())

words = []

for _ in range(n):
    words.append(input())

dict = {}

for word in words:
  k = len(word)-1
  for s in word:
    if s in dict:
      dict[s] += pow(10,k)
    else:
      dict[s] = pow(10,k)
    k -= 1

