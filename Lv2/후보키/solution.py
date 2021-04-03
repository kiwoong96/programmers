from itertools import combinations


def solution(relation):
    answer = 0
    answer_list = []
    for i in range(1, len(relation)):

        data = list(combinations(range(len(relation[0])), i))
        for now in data:

            data_set = []
            for j in range(len(relation)):
                if [relation[j][now[k]] for k in range(len(now))] not in data_set:
                    data_set.append([relation[j][now[k]] for k in range(len(now))])
                else:
                    break
            print(now, data_set)
            is_Same = False
            print(answer_list)
            if len(data_set) == len(relation):
                for k in range(len(now)):
                    check = list(combinations(now, k))
                    for tmp in check:
                        if tmp in answer_list:
                            is_Same = True
                            break
                    if is_Same == True:
                        break
                if is_Same == False:
                    answer_list.append(now)
                    answer += 1

            print(answer)

    return answer