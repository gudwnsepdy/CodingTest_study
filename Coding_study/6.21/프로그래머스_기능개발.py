from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)


    while 1:
        if not progresses:
            break
        cnt = 0

        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        while 1:
            if not progresses:
                break
            num = progresses.popleft()
            if num >= 100:
                cnt += 1
                speeds.popleft()
            else:
                progresses.appendleft(num)
                break

        if cnt:
            answer.append(cnt)
    return answer

# print(solution([93, 30, 55],[1, 30, 5]))