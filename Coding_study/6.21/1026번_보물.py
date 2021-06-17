n = int(input())
Aarr = list(map(int, input().split()))
Barr = list(map(int, input().split()))

Aarr.sort(reverse=True)
Barr.sort()

# print(Aarr)
# print(Barr)

res = 0

for i in range(n):
    res += Aarr[i] * Barr[i]

print(res)