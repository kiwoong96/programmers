N, K = map(int,input().split())

dp = [0 for _ in range(10001)]

coins = []
dp[0] = 1
for i in range(N):
    coins.append(int(input()))

for i in coins:
    for j in range(i,K+1):
        dp[j] += dp[j-i]


print(dp[K])