n = int(input())

now_score = 0
for _ in range(n):
    now_score = 0
    total = 0
    ox = str(input())
    for i in ox:
        if i == 'O':
            now_score += 1
            total += now_score
        else:
            now_score = 0
    print(total)