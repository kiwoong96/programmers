def solution(number, k):
    answer = ''
    collected = []

    for (i, num) in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1

        if k == 0:
            collected.append(number[i:])
            break

        collected.append(num)

    if k > 0:
        collected = collected[:-k]
    answer = ''.join(collected)
    return answer