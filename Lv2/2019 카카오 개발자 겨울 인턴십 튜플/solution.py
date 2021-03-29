def solution(s):
    answer = []

    my_set = {}

    s = s[2:-2]
    s_list = list(s.split('},{'))
    # print(s_list)
    for idx in range(len(s_list)):
        s_list[idx] = list(map(int, s_list[idx].split(',')))

    for now in s_list:
        for k in now:
            if k in my_set:
                my_set[k] += 1
            else:
                my_set[k] = 1

    result = sorted(my_set.items(), key=lambda x: x[1], reverse=True)

    for data in result:
        answer.append(data[0])

    return answer

