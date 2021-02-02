N, K = map(int,input().split())

bags = [[0,0]]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N):
    bags.append(list(map(int,input().split())))

for i in range(1,N+1):
    for j in range(1,K+1):
        if j >= bags[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-bags[i][0]] + bags[i][1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])
