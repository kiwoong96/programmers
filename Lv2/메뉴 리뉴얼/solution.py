from itertools import combinations


def solution(orders, course):
    answer = []
    # course에 맞게
    my_order = []
    for now in orders:
        tmp = []
        for x in now:
            tmp.append(x)
        tmp.sort()
        my_order.append(tmp)

    for c in course:
        comb = {}
        for order in my_order:
            data = list(combinations(order, c))
            for now in data:
                tmp = ''.join(now)
                if tmp in comb:
                    comb[tmp] += 1
                else:
                    comb[tmp] = 1

        for key, value in comb.items():
            if value == max(comb.values()) and value >= 2:
                answer.append(key)

    answer.sort()
    return answer