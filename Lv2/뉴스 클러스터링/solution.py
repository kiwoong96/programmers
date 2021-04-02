import re


def s_to_list(str1):
    str1_list = []
    for i in range(len(str1) - 1):
        now = re.sub('[^A-Za-z]', '', str1[i:i + 2])
        if len(now) == 2:
            str1_list.append(now.upper())

    result = {}
    for now in str1_list:
        if now in result:
            result[now] += 1
        else:
            result[now] = 1

    return result


def solution(str1, str2):
    answer = 0
    str1_list = s_to_list(str1)
    str2_list = s_to_list(str2)
    if str1_list == str2_list:
        return 65536

    first = 0
    for now in str1_list:
        if now in str2_list:
            first += min(str1_list[now], str2_list[now])

    for now in str1_list:
        if now in str2_list:
            str2_list[now] = max(str1_list[now], str2_list[now])
        else:
            str2_list[now] = str1_list[now]
    second = sum(str2_list.values())

    answer = int(first / second * 65536)

    return answer