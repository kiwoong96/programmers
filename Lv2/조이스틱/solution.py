def solution(name):
    data = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    answer = 0
    idx = 0
    print(data)
    while True:
        answer += data[idx]
        data[idx] = 0

        # 이름 완성
        if sum(data) == 0:
            break

        left, right = 1, 1
        while data[idx - left] == 0:
            left += 1

        while data[idx + right] == 0:
            right += 1

        if left < right:
            idx -= left
        else:
            idx += right
        answer += min(left, right)
    return answer