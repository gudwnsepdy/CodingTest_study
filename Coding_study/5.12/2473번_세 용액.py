import sys
n = int(input())
liquid = list(map(int,input().split()))
liquid.sort()
answer = sys.maxsize
answer_1 = 0
answer_2 = 1
answer_3 = n-1


for n1 in range(len(liquid) - 2):
    left = n1 + 1
    right = n - 1

    while(left < right):
        tmp = liquid[left] + liquid[right] + liquid[n1]

        if abs(tmp) <= abs(answer):
            # print(liquid[left], liquid[right] , liquid[n1], tmp)
            answer = tmp
            answer_1 = n1
            answer_2 = left
            answer_3 = right
            if answer == 0:
                print(*(sorted([liquid[answer_1], liquid[answer_2], liquid[answer_3]])))
                exit()
        if tmp < 0:
            left += 1
        elif tmp > 0:
            right -= 1


print(*(sorted([liquid[answer_1], liquid[answer_2], liquid[answer_3]])))