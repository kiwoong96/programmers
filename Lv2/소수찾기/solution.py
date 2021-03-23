from itertools import permutations
import math


def check(number):
    k = math.sqrt(number)
    if number < 2:
        return False

    for i in range(2, int(k) + 1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = []

    tmp_result = []
    for i in range(1, len(numbers) + 1):
        tmp_data = list(map(''.join, permutations(numbers, i)))

        for now in list(set(tmp_data)):
            if check(int(now)):
                answer.append(int(now))

    return len(list(set(answer)))