def solution(s):
    data = list(map(int, s.split(' ')))

    answer = ''
    answer += str(min(data)) + ' '
    answer += str(max(data))
    return answer