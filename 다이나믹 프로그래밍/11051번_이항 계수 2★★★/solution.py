"""N,K = map(int,input().split())

dp = [0 for _ in range(N+1)]

dp[0] = 1

for i in range(K,0,-1):
    dp[K+1-i] = (dp[K-i]*(i+N-K)/i)%10007

print(int(dp[K]))"""

N, K = map(int,input().split())


dp = [[0] for _ in range(1001)]

for i in range(1,N+1):
    for j in range(0,N):
        if j==0:
            dp[i][j] = 1
        elif j== N:
            dp[i]
