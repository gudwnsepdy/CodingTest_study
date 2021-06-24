answer = 0
def cal(num, idx, target,numbers,pm):
    global answer
    num += numbers[idx] * pm
    if idx == len(numbers) - 1:
        if num == target:
            answer += 1
        return
    cal(num,idx + 1, target, numbers, pm)
    cal(num, idx + 1, target, numbers, -1 * pm)

def solution(numbers, target):
    global answer
    cal(0,0,target,numbers, 1)
    cal(0, 0, target, numbers, -1)

    return answer

print(solution([1, 1, 1, 1, 1], 3))