import math


def solution(arr):
    answer = 0
    stack = arr

    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        c = a * b // math.gcd(a, b)
        stack.append(c)

    return stack[0]


