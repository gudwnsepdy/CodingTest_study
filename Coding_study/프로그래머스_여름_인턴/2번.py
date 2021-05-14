def solution(t, r):
    answer = []
    tmp = []
    arr = list(zip([i for i in range(len(t))], t, r))
    cnt = -1
    waiting = []

    while(len(tmp) != len(t)):
        cnt += 1

        for a in arr:
            if a[1] == cnt:
                waiting.append(a)
        waiting = sorted(waiting, key=lambda x: (x[2], x[1], x[0]))
        if len(waiting) != 0:
            tmp.append(waiting[0])
            del waiting[0]


    for id in tmp:
        answer.append(id[0])


    return answer


print(solution([0, 1, 3, 0], [0, 1, 2, 3]))
print(solution([7, 6, 8, 1], [0, 1, 2, 3]))
