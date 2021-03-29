from itertools import combinations


def solution(clothes):
    answer = 0
    clothes_dict = dict()

    for data in clothes:
        if data[1] in clothes_dict:
            clothes_dict[data[1]] += 1
        else:
            clothes_dict[data[1]] = 1

    """
    result = 0

    for i in range(1,len(clothes_dict)+1):
        comb = list(combinations(clothes_dict.keys(),i))
        for now in comb:
            tmp_result = 1
            for idx in now:
                tmp_result *= clothes_dict[idx]
            result += tmp_result

    print(result)
    """

    result = 1

    for data in clothes_dict.values():
        result *= (data + 1)

    return result - 1