
n, k = map(int,input().split())


belt = list(map(int,input().split()))
robot = [0 for _ in range(2 * n)]



cnt = 0
while(1):
    cnt += 1

    temp_belt = belt[2*n - 1]
    del belt[2*n - 1]
    belt.insert(0,temp_belt)
    robot[n - 1] = 0

    temp_robot = robot[2 * n - 1]
    del robot[2 * n - 1]
    robot.insert(0, temp_robot)

    #2
    for i in range(n-1, -1, -1):
        if robot[i] == 1:
            if i == n - 1:
                robot[i] = 0
            else:
                if robot[i + 1] == 0 and belt[i + 1] > 0:
                    robot[i + 1] = 1
                    robot[i] = 0
                    belt[i+1] -= 1
                    if belt[i + 1] < 0:
                        belt[i + 1] = 0


    #3
    if robot[0] == 0 and belt[0] > 0:
        robot[0] = 1
        belt[0] -=1
        if belt[0] < 0:
            belt[0] = 0


    if belt.count(0) >= k:
        break

print(cnt)

"""
5 8
100 99 60 80 30 20 10 89 99 100
"""