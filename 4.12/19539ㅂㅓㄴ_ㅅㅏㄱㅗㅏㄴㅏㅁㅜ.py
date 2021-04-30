n = int(input())

apple = list(map(int, input().split()))

for i in range(len(apple)):
    tmp = apple[i]
    while(tmp >= 3):
        if tmp - 3 >= 0:
            tmp -= 3
    apple[i] = tmp

print(apple)