"""import sys
input = sys.stdin.readline



def solution(n):
    dp = [0 for _ in range(N+1)]


    answer = 0
    return answer

n = 4
result  = solution(n)
print(result)"""

"""
def solution(N, number):
    dp = [1e9 for _ in range(300001)]
    k = N
    i = 1
    while k < 300001:
        dp[k] = i
        k = str(k)
        k += str(N)
        k = int(k)
        i += 1
    for j in range(0, 300001):
        tmp_j = j - N
        if tmp_j >= 0 and dp[tmp_j] != -1:
            dp[j] = min(dp[j], dp[tmp_j] + 1)

        tmp_j = j + N
        if tmp_j < 300001 and dp[tmp_j] != -1:
            dp[j] = min(dp[j], dp[tmp_j] + 1)

        tmp_j = j * N
        if tmp_j < 300001 and dp[tmp_j] != -1:
            dp[j] = min(dp[j], dp[tmp_j] + 1)

        if j % N == 0 and dp[j // N] != -1:
            dp[j] = min(dp[j], dp[j // N] + 1)
    return dp



dp = solution(5,12)
print(dp[:100])
print(dp[12])
"""
stack = [1,2,3,4,5]

print(stack.pop())

