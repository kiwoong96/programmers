def change_number(n, number):
    # n진법 number값
    result = ''
    if number == 0:
        return '0'
    while number >= 1:
        if number % n < 10:
            result += str(number % n)
        else:
            result += chr(number % n + 65 - 10)
        number //= n

    return result[::-1]


def solution(n, t, m, p):
    answer = ''
    result = ''
    idx = 0
    while len(result) < t * m:
        result += change_number(n, idx)
        idx += 1
    for i in range(t):
        answer += result[i * m + (p - 1)]

    return answer