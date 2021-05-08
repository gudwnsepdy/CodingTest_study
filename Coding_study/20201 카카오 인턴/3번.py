def solution(n, k, cmd):
    answer = ''
    arr = ["O" for _ in range(n)]
    cursor = k
    trash = []

    for i in cmd:
        # print(i, end= " cursor: ")
        if i == "C":
            arr[cursor] = "X"
            trash.append(cursor)
            flag = False
            for t in range(cursor , n):
                if arr[t] == "O":
                    cursor = t
                    flag = True
                    break
            if not flag:
                for t in range(cursor, -1, -1):
                    if arr[t] == "O":
                        cursor = t
                        break
            # if cursor == len(arr) - 1:
            #     cursor -= 1
            # else:
            #     cursor += 1
        if i == "Z":
            arr[trash[-1]] = "O"
            del trash[-1]

        if i[0] == "D":
            a, b = i.split(" ")
            b = int(b)
            for t in range(1,n):
                if arr[cursor + t] == "O":
                    b -= 1
                    if b == 0:
                        cursor += t
                        break


        elif i[0] == "U":
            a, b = i.split(" ")
            b = int(b)
            for t in range(1,n):
                if arr[cursor - t] == "O":
                    b -= 1
                    if b== 0:
                        cursor -= t
                        break


        # print(cursor,arr)
    # print(arr)
    answer = "".join(arr)
    return answer

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
# print(solution(4,1,["U 1","C","C","D 1", "C","Z","Z","Z","C","C","C"]))
