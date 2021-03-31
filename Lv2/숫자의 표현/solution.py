def solution(n):
    answer = 0
    sumation = 1
    start = 1
    end = 1

    while end <= n:
        if sumation > n:
            sumation -= start
            start += 1
        elif sumation < n:
            end += 1
            sumation += end
        else:
            # print(start, end,sumation)
            answer += 1
            end += 1
            sumation += end

    return answer