def dic_find(sub_msg, dic):
    if sub_msg in dic:
        return True
    return False


def solution(msg):
    answer = []
    dic = {}
    for i in range(1, 27):
        dic[chr(64 + i)] = i
    dic_idx = 27
    msg_idx = 0
    k = 0
    while msg_idx < len(msg):
        length = 1
        sub_msg = msg[msg_idx:msg_idx + length]
        while True:

            if dic_find(sub_msg, dic) and msg_idx + length <= len(msg):
                length += 1
                sub_msg = msg[msg_idx:msg_idx + length]
            else:
                answer.append(dic[msg[msg_idx:msg_idx + length - 1]])
                if not dic_find(sub_msg, dic):
                    dic[sub_msg] = dic_idx
                dic_idx += 1
                msg_idx += length - 1
                break
    return answer