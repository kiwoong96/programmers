N, K = map(int,input().split())

coins = []
dp = [10001 for _ in range(K+1)]

for i in range(N):
    coins.append(int(input()))

##Point!!
coins.sort()



for i in range(N):
    for j in range(coins[i],K+1):
        if j%coins[i] == 0:
            dp[j] = min(dp[j],j//coins[i])
        else:
            dp[j] = min(dp[j-coins[i]]+dp[coins[i]],dp[j])

if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])



