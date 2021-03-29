def solution(people, limit):
    answer = 0
    count = [0 for _ in range(241)]

    for idx in people:
        count[idx] += 1

    idx = 40

    while idx <= limit:
        if count[idx] != 0:
            count[idx] -= 1
            for best_idx in range(limit - idx, -1, -1):
                if count[best_idx] != 0:
                    count[best_idx] -= 1
                    break
            answer += 1
        else:
            idx += 1

    return answer