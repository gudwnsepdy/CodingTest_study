ans = 0

def cal(numbers, target, num, l):
    global ans
    if l == len(numbers):
        if num == target:
            ans += 1
            return 1
        else:
            return 0
    cal(numbers, target, num - numbers[l], l + 1)
    cal(numbers, target, num + numbers[l], l + 1)

def solution(numbers, target):

    cal(numbers, target, 0, 0)
    return ans

print(solution([1,1,1,1,1], 3))