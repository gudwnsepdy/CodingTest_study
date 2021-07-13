testCase = int(input())

for test in range(testCase):
    arr = list(map(str, input().split()))
    soundList = []
    while 1:
        ment = str(input())
        if ment == "what does the fox say?":
            break
        ment = list(map(str, ment.split()))
        soundList.append(ment[-1])

    final = []
    for i in arr:
        if i not in soundList:
            final.append(i)
    print(*final)