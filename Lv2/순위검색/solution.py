from itertools import combinations
from collections import defaultdict


def solution(info, queries):
    answer = []
    info_dict = defaultdict(list)
    for now in info:
        info_item = now.split()
        info_key = info_item[:-1]
        info_value = int(info_item[-1])
        for i in range(5):
            for c in combinations(info_key, i):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_value)

    for keys in info_dict.keys():
        info_dict[keys].sort()

    for query in queries:
        query = query.split()
        query_key = query[:-1]
        query_value = int(query[-1])

        for i in range(3):
            query_key.remove('and')
        while '-' in query_key:
            query_key.remove('-')

        query_key = ''.join(query_key)

        if query_key in info_dict:
            now = info_dict[query_key]

            if len(now) > 0:
                start, end = 0, len(now)
                while start < end:
                    mid = (start + end) // 2
                    if now[mid] >= query_value:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(now) - start)

        else:
            answer.append(0)

    return answer