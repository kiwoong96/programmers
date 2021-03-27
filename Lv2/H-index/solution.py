def solution(citations):
    citations.sort(reverse=True)

    answer = []

    for i in range(len(citations)):
        if min(citations[i], i + 1) not in answer:
            answer.append(min(citations[i], i + 1))

    return max(answer)