def solution(msg):
    answer = []
    dic = {chr(ord('A') + i): (i + 1) for i in range(26)}

    count = 27
    i = 0
    now = ''

    while i < len(msg):
        now += msg[i]
        if now in dic:
            i += 1
            continue
        dic[now] = count
        count += 1

        s = now[:-1]
        answer.append(dic[s])
        now = ''

    answer.append(dic[now])
    return answer


if __name__ == '__main__':
    msgs = [
        'KAKAO', 'TOBEORNOTTOBEORTOBEORNOT', 'ABABABABABABABAB'
    ]

    for msg in msgs:
        print(msg, solution(msg))
