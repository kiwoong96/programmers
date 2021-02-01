N, M = map(int,input().split())

arr = []

for i in range(N):
    arr.append(list(map(int,input().split())))


dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        dp[i+1][j+1] = arr[i][j]

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + dp[i][j]

print(dp[N][M])