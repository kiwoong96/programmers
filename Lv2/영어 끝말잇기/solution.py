def solution(n, words):
    answer = [0, 0]
    before = set()
    before_word = words[0][0]
    for idx in range(len(words)):
        if before_word == words[idx][0] and words[idx] not in before:
            before.add(words[idx])
            before_word = words[idx][-1]
        else:
            answer[0] = idx % n + 1
            answer[1] = idx // n + 1
            break

    return answer