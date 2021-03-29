def condition2(n):
    count = 0
    dec_to_binary = ''

    while n > 1:
        dec_to_binary += str(n % 2)
        n //= 2

    dec_to_binary += str(n)

    for k in dec_to_binary:
        if k == '1':
            count += 1
    return count


def solution(n):
    count1 = condition2(n)
    while True:
        n = n + 1
        count2 = condition2(n)
        if count1 == count2:
            break

    return n