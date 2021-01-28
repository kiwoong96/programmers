N = int(input())


dp = [[0 for _ in range(31)] for _ in range(31)]

for i in range(1,31):
    for j in range(1,31):
        if i == j:
            dp[i][j] = 1
        elif i == 1:
            dp[i][j] = dp[i][j-1] + 1
        elif j>i:
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]




for i in range(N):
    N,M = list(map(int,input().split()))
    print(dp[N][M])

