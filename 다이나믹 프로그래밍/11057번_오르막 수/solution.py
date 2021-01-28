N = int(input())

dp = [[0 for _ in range(10)] for _ in range(10001)]


for i in range(10001):
    for j in range(10):
        if i == 0:
            dp[i][j] = 0
        elif i == 1 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(sum(dp[N])%10007)


