"""N,K = map(int,input().split())

dp = [0 for _ in range(N+1)]

dp[0] = 1

for i in range(K,0,-1):
    dp[K+1-i] = (dp[K-i]*(i+N-K)/i)%10007

print(int(dp[K]))"""

N, K = map(int,input().split())


dp = [[1] for _ in range(1001)]

for i in range(1,N+1):
    for j in range(1,i+1):
        if j==i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i-1][j-1] + dp[i-1][j])

print(dp[N][K]% 10007)