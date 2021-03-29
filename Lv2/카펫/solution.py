import math


def solution(brown, yellow):
    answer = []

    sero, garo = 0, 0

    for i in range(1, math.ceil(math.sqrt(yellow)) + 1):
        if yellow % i == 0:
            sero = i
            garo = yellow // i

            if brown == sero * 2 + garo * 2 + 4:
                break

    return garo + 2, sero + 2