def solution(record):
    answer = []
    IdName = {}
    for i in range(len(record) - 1, -1, -1):
        order = record[i].split()
        if (order[0] == 'Enter' or order[0] == 'Change') and order[-2] not in IdName:
            IdName[order[-2]] = order[-1]

    for data in record:
        order = data.split()[0]
        message = ''
        if order == 'Enter':
            message = IdName[data.split()[-2]] + '님이 들어왔습니다.'
        elif order == 'Leave':
            message = IdName[data.split()[-1]] + '님이 나갔습니다.'
        else:
            continue
        answer.append(message)

    return answer