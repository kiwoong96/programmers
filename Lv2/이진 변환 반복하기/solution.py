def dec_to_bin(n):
    result = ''
    while n > 1:
        result += str(n % 2)
        n //= 2
    result += str(n)
    result = result[::-1]

    return result


def bin_to_dec(s):
    result = ''
    for i in s:
        if i == '1':
            result += '1'

    length = len(result)

    number = dec_to_bin(length)

    return len(s) - length, number


def solution(s):
    answer = []
    count = 0
    sumation = 0

    while s != '1':
        count += 1
        sumation += bin_to_dec(s)[0]
        s = bin_to_dec(s)[1]

    return count, sumation