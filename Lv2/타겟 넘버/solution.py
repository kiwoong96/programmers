result = 0
def DFS(idx, tmp_result, numbers, target):
    global result

    if idx == len(numbers):
        if tmp_result == target:
            result += 1
        return

    tmp_result += numbers[idx]
    DFS(idx + 1, tmp_result, numbers, target)

    tmp_result -= numbers[idx]

    tmp_result -= numbers[idx]
    DFS(idx + 1, tmp_result, numbers, target)


def solution(numbers, target):
    answer = 0
    DFS(0, 0, numbers, target)
    return result