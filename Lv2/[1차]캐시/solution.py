from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for data in cities:
        data = data.upper()
        if data in cache:
            cache.remove(data)
            cache.append(data)
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.popleft()

            cache.append(data)
            answer += 5

    return answer