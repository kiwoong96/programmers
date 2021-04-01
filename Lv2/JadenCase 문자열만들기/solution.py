def solution(s):
    answer = ''
    datas = list(s.split(' '))
    for now in datas:
        for i in range(len(now)):
            if i == 0:
                answer += now[i].upper()
            else:
                answer += now[i].lower()
        answer += ' '

    return answer[:-1]