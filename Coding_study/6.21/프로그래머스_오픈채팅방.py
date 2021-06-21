def solution(record):
    answer = []
    name = dict()
    adminMSG = []
    # 0 enter 1 leave
    for msg in record:
        spaceCount = msg.count(" ")
        if spaceCount == 1:
            l, uid = msg.split()
            adminMSG.append([1, uid])
        else:
            command, uid, nick = msg.split()
            if command == "Enter":
                adminMSG.append([0, uid])
                name[uid] = nick
            else:
                name[uid] = nick

    for what, who in adminMSG:
        if what == 0:
            answer.append(str(name[who])+"님이 들어왔습니다.")
        else:
            answer.append(str(name[who]) + "님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))