def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        result = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                result += 1
            else:
                result += 1
                break

        answer.append(result)

    answer.append(0)

    return answer